from src.sentiment_analysis import analyze_sentiment_vader, analyze_sentiment_textblob

def test_analyze_sentiment_vader():
    text = "I love this bank service."
    label, score = analyze_sentiment_vader(text)
    assert label == 'positive'
    assert score > 0

def test_analyze_sentiment_textblob():
    text = "I hate the delays."
    label, polarity, subjectivity = analyze_sentiment_textblob(text)
    assert label == 'negative'
    assert polarity < 0
