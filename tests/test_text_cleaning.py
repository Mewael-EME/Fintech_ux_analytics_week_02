from src.text_cleaning import clean_text

def test_clean_text():
    input_text = "Hello!!! This is a test... Visit http://example.com."
    cleaned = clean_text(input_text)
    assert "http" not in cleaned
    assert "hello" in cleaned
    assert "test" in cleaned
    assert "!!!" not in cleaned
