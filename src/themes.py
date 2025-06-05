from sklearn.feature_extraction.text import TfidfVectorizer

# Define common theme clusters
theme_keywords = {
    "Account Access": ["login", "password", "reset", "locked"],
    "Transactions": ["transfer", "transaction", "processing", "delay"],
    "UI/UX": ["design", "crash", "navigation", "layout"],
    "Support": ["support", "agent", "help", "response"],
    "Features": ["feature", "dark mode", "wallet", "QR"]
}

def extract_keywords(text_series, top_n=5):
    tfidf = TfidfVectorizer(max_df=0.9, min_df=5, ngram_range=(1, 2), stop_words="english")
    tfidf_matrix = tfidf.fit_transform(text_series)
    feature_names = tfidf.get_feature_names_out()
    keywords_per_doc = []

    for i in range(tfidf_matrix.shape[0]):
        row = tfidf_matrix[i].tocoo()
        sorted_items = sorted(zip(row.col, row.data), key=lambda x: -x[1])[:top_n]
        keywords_per_doc.append([feature_names[i] for i, _ in sorted_items])

    return keywords_per_doc

def map_themes(keywords):
    themes = set()
    for word in keywords:
        for theme, keys in theme_keywords.items():
            if any(k in word for k in keys):
                themes.add(theme)
    return list(themes)
 
