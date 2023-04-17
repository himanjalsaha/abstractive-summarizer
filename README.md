# abstractive-summarizer
# Flask Text Summarization App

This is a Flask web application that uses the Pegasus model for text summarization. The app takes in text as input, processes it through the Pegasus model, and returns a summarized version of the text.

## Prerequisites
- Flask
- transformers
- PegasusForConditionalGeneration
- PegasusTokenizer

## Setup
1. Clone this repository
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Run the app using `python app.py`

## Usage
1. Enter the text to be summarized in the input box on the home page.
2. Click on the "Summarize" button to submit the text.
3. The summarized text will be displayed on the results page.

## Note
- The Pegasus model used in this app is `google/pegasus-xsum`.
- The summarizer pipeline is created with `min_length=30` and `max_length=150`.
- The app runs in debug mode, which is not recommended for production use.
