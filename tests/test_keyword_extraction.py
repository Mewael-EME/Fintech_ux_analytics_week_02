from src.keyword_extraction import extract_keywords

def test_extract_keywords():
    corpus = [
        "The login process is slow and unreliable.",
        "Customer support was very helpful and responsive.",
        "UI crashes frequently when transferring money."
    ]
    keywords = extract_keywords(corpus, top_n=5)
    assert any("login" in kw for kw in keywords)
    assert any("support" in kw for kw in keywords)
