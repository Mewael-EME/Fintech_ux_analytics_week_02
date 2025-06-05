import pandas as pd
from src.preprocessing import preprocess_text
from src.sentiment import analyze_sentiment
from src.themes import extract_keywords, map_themes

# Load data
df = pd.read_csv("data/reviews.csv")  # Ensure this file exists

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

# Save results
df[["review_id", "review_text", "sentiment_label", "sentiment_score", "identified_themes"]].to_csv(
    "data/task2_output.csv", index=False
)

print("Task 2 completed. Output saved to data/task2_output.csv")
