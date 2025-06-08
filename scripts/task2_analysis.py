import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.preprocessing import preprocess_text
from src.sentiment import analyze_sentiment
from src.themes import extract_keywords, map_themes, sklearn_lda_topics

# Load data
df = pd.read_csv("data/ethiopian_bank_reviews_clean.csv")  # Ensure this file exists

# Print original columns
print(" Original Columns:", df.columns.tolist())

if 'review' in df.columns:
    df = df.rename(columns={"review": "review_text"})

# Add review_id (assumes row index is unique and can act as ID)
df["review_id"] = df.index + 101  # start from 101 as in your sample

print(" Original Columns:", df.columns.tolist())


# Preprocess text
df["clean_text"] = df["review"].apply(preprocess_text)

# Sentiment analysis
sentiment_results = df["review"].apply(analyze_sentiment)
df["sentiment_label"] = sentiment_results.apply(lambda x: x["label"])
df["sentiment_score"] = sentiment_results.apply(lambda x: x["score"])

# Keyword extraction
df["top_keywords"] = extract_keywords(df["clean_text"])

# Theme identification (rule-based mapping from keywords)
df["identified_themes"] = df["top_keywords"].apply(map_themes)

# ----- LDA Topic Modeling Integration -----

# Run LDA topic modeling on cleaned text, extracting 5 topics
lda_topics = sklearn_lda_topics(df["clean_text"], num_topics=5)

print("\n LDA Topic Modeling Results:")
for idx, words in lda_topics:
    print(f"Topic {idx + 1}: {', '.join(words)}")

# Save LDA topics to CSV for inspection
topics_df = pd.DataFrame({
    "topic_id": [idx + 1 for idx, _ in lda_topics],
    "keywords": [", ".join(words) for _, words in lda_topics]
})
topics_df.to_csv("data/themes_lda.csv", index=False)
print(" Saved LDA topics to data/themes_lda.csv")

# -------------------------------------------

# Save final analysis CSV with required columns
df[["review_id", "review", "sentiment_label", "sentiment_score", "identified_themes"]].rename(
    columns={"review": "review_text"}
).to_csv("data/task2_output.csv", index=False)

print(" Task 2 completed. Output saved to data/task2_output.csv")
