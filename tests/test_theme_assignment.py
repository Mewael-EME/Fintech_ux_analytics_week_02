from src.theme_assignment import assign_themes

def test_assign_themes():
    keywords = ['login', 'password', 'slow', 'transfer', 'support']
    themes = assign_themes(keywords)
    assert 'Account Access Issues' in themes
    assert 'Transaction Performance' in themes
    assert 'Customer Support' in themes
