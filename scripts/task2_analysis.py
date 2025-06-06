import sys
import os
import pandas as pd

# Ensure src module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import preprocess_text
from src.sentiment import analyze_sentiment
from src.themes import extract_keywords, map_themes

# Load data
df = pd.read_csv("data/ethiopian_bank_reviews_clean.csv")  # Make sure this exists and has required content

# Print original columns
print("🔍 Original Columns:", df.columns.tolist())

# Rename to match desired schema if needed
if 'review' in df.columns:
    df = df.rename(columns={"review": "review_text"})

# Add review_id (assumes row index is unique and can act as ID)
df["review_id"] = df.index + 101  # start from 101 as in your sample

# Preprocess text
df["clean_text"] = df["review_text"].apply(preprocess_text)

# Sentiment analysis
sentiment_results = df["review_text"].apply(analyze_sentiment)
df["sentiment_label"] = sentiment_results.apply(lambda x: x["label"])
df["sentiment_score"] = sentiment_results.apply(lambda x: x["score"])

# Keyword extraction
df["top_keywords"] = extract_keywords(df["clean_text"])

# Theme identification
df["identified_themes"] = df["top_keywords"].apply(map_themes)

# Select only required columns and save
df[["review_id", "review_text", "sentiment_label", "sentiment_score", "identified_themes"]].to_csv(
    "data/task2_output.csv", index=False
)

print("Task 2 completed. Output saved to data/task2_output.csv")
