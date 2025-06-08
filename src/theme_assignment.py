def assign_themes(keywords):
    theme_keywords = {
        'Account Access Issues': ['login', 'password', 'access', 'account', 'lockout', 'unlock'],
        'Transaction Performance': ['slow', 'delay', 'transfer', 'transaction', 'failed', 'processing'],
        'User Interface & Experience': ['ui', 'user interface', 'design', 'navigation', 'crash', 'bug', 'responsive'],
        'Customer Support': ['support', 'help', 'service', 'response', 'agent', 'call', 'email'],
        'Feature Requests': ['feature', 'add', 'improve', 'request', 'update', 'new']
    }
    themes_found = set()
    for theme, kw_list in theme_keywords.items():
        for kw in kw_list:
            if kw in keywords:
                themes_found.add(theme)
    return list(themes_found) if themes_found else ['Miscellaneous']
