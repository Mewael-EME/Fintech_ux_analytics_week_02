# src/reviews_utils.py
from google_play_scraper import reviews, Sort
import pandas as pd
import time

def scrape_bank_reviews(app_id, bank_name, max_reviews= 700):
    all_reviews = []
    count = 0
    batch_size = 100
    continuation_token = None

    while count < max_reviews:
        result, continuation_token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=continuation_token
        )
        if not result:
            break
        
        for r in result:
            all_reviews.append({
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'],
                'bank': bank_name,
                'source': 'Google Play'
            })
        
        count += len(result)
        if not continuation_token:
            break
        
        time.sleep(1)  # be polite to server

    return pd.DataFrame(all_reviews)

import re

def preprocess_reviews(df):
    # Remove duplicates and missing
    df = df.drop_duplicates().dropna(subset=['review', 'rating', 'date'])

    # Normalize dates
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Drop rows where date conversion failed (NaT)
    df = df.dropna(subset=['date'])

    # Define a regex pattern to detect only allowed characters (letters, numbers, basic punctuation, space)
    # This pattern *excludes* emojis and many special symbols
    valid_pattern = re.compile(r'^[a-zA-Z0-9\s.,!?\'\"-:;()]+$')

    # Keep rows where review matches the valid pattern
    mask_valid_review = df['review'].apply(lambda x: bool(valid_pattern.match(x.strip())))

    df = df[mask_valid_review]

    df = df.reset_index(drop=True)
    return df

