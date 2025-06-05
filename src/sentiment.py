from transformers import pipeline

# Load once and reuse
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    return sentiment_pipeline(text[:512])[0]  # truncate long texts
 
