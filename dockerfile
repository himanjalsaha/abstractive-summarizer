# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 80 for the Flask app
EXPOSE 80

# Define environment variable
ENV FLASK_APP=main.py

# Run the app when the container launches
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main:app"]
