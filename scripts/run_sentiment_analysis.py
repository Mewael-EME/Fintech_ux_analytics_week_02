import pandas as pd
from src.text_cleaning import clean_text
from src.sentiment_analysis import analyze_sentiment_vader, analyze_sentiment_textblob

# Load data
df = pd.read_csv('data/ethiopian_bank_reviews_clean.csv')

# Preprocess text
df['cleaned_text'] = df['review'].apply(clean_text)

# Analyze sentiment using VADER
df[['vader_label', 'vader_score']] = df['cleaned_text'].apply(lambda x: pd.Series(analyze_sentiment_vader(x)))

# Analyze sentiment using TextBlob
df[['textblob_label', 'textblob_polarity', 'textblob_subjectivity']] = df['cleaned_text'].apply(lambda x: pd.Series(analyze_sentiment_textblob(x)))

# Aggregate sentiment by bank and rating
aggregation = df.groupby(['bank', 'rating'])['vader_score'].mean().reset_index()
aggregation.to_csv('output_data/sentiment_aggregation.csv', index=False)

# Save detailed results
df.to_csv('output_data/sentiment_analysis_results.csv', index=False)
