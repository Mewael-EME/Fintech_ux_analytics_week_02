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
