# src/themes.py

import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text_series):
    """
    Example function to extract keywords using spaCy noun chunks.
    Modify or replace this function as per your original implementation.
    """
    keywords_list = []
    for doc in nlp.pipe(text_series, disable=["parser", "ner"]):
        keywords = [chunk.text.lower() for chunk in doc.noun_chunks]
        keywords_list.append(keywords)
    return keywords_list

def map_themes(keywords_list):
    """
    Map keywords to predefined themes.
    Modify theme mapping logic as needed.
    """
    theme_map = {
        "account": "Account Access Issues",
        "login": "Account Access Issues",
        "transfer": "Transaction Performance",
        "slow": "Transaction Performance",
        "ui": "User Interface & Experience",
        "interface": "User Interface & Experience",
        "support": "Customer Support",
        "feature": "Feature Requests",
        "crash": "Reliability",
    }
    themes_per_review = []
    for keywords in keywords_list:
        themes = set()
        for kw in keywords:
            for key, theme in theme_map.items():
                if key in kw:
                    themes.add(theme)
        themes_per_review.append(list(themes))
    return themes_per_review

def sklearn_lda_topics(clean_text_series, num_topics=5, num_top_words=7):
    """
    Perform LDA topic modeling on cleaned text using scikit-learn.

    Args:
        clean_text_series (pd.Series): Preprocessed text data.
        num_topics (int): Number of topics to extract.
        num_top_words (int): Number of top words to display per topic.

    Returns:
        List of tuples: (topic_index, list_of_top_words)
    """
    # Vectorize text data to document-term matrix
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(clean_text_series)

    # Create LDA model and fit
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)

    # Get feature names (words)
    feature_names = vectorizer.get_feature_names_out()

    # Extract top words per topic
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        top_features_ind = topic.argsort()[:-num_top_words - 1:-1]
        top_words = [feature_names[i] for i in top_features_ind]
        topics.append((topic_idx, top_words))
    return topics

# Optionally, you can add more helper functions here or your existing ones
