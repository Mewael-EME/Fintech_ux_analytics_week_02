from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(corpus, top_n=30):
    vectorizer = TfidfVectorizer(min_df=1, max_df=1.0, ngram_range=(1, 2), stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    tfidf_dict = dict(zip(feature_names, tfidf_scores))
    sorted_keywords = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)
    top_keywords = [kw for kw, score in sorted_keywords[:top_n]]
    return top_keywords
