import pandas as pd
from src.text_cleaning import clean_text
from src.keyword_extraction import extract_keywords
from src.theme_assignment import assign_themes

# Load data
df = pd.read_csv('data/ethiopian_bank_reviews_clean.csv')

# Preprocess text
df['cleaned_text'] = df['review'].apply(clean_text)

# Assign themes per bank
bank_themes = {}
for bank in df['bank'].unique():
    bank_reviews = df[df['bank'] == bank]['cleaned_text']
    keywords = extract_keywords(bank_reviews)
    themes = assign_themes(keywords)
    bank_themes[bank] = themes

# Map themes back to reviews
df['themes'] = df['bank'].map(bank_themes)

# Save results
df.to_csv('output_data/thematic_analysis_results.csv', index=False)
