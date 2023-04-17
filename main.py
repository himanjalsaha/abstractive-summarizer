from flask import Flask,render_template,request
from transformers import pipeline
from transformers import PegasusForConditionalGeneration,PegasusTokenizer

app =Flask(__name__)

model_name = "google/pegasus-xsum"

Pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)


summarizer = pipeline("summarization",model=model_name,tokenizer=Pegasus_tokenizer,framework='pt')

@app.route('/')
def home():
    
    return render_template('base.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        data=request.form.get('data')
        summary = summarizer(data,min_length=30,max_length=150)
        summary=str(summary)[18:-3]

    return render_template('result.html',summary=summary,data=data)    


if __name__=="__main__":
    app.run(debug=True)