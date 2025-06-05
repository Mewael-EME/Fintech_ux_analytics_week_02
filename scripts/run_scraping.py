# scripts/run_scraping.py
import os
import sys
import pandas as pd

# add src to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from reviews_utils import scrape_bank_reviews

def main():
    apps = {
        'com.combanketh.mobilebanking': 'Commercial Bank of Ethiopia Mobile',
        'com.boa.boaMobileBanking': 'Bank of Abyssinia Mobile',
        'com.dashen.dashensuperapp': 'Dashen Bank Mobile'
    }

    all_dfs = []
    for app_id, bank_name in apps.items():
        print(f"Scraping reviews for {bank_name} ...")
        df = scrape_bank_reviews(app_id, bank_name, max_reviews=700)
        all_dfs.append(df)

    df_all = pd.concat(all_dfs, ignore_index=True)

    # Save raw data locally in data/ folder
    os.makedirs('data', exist_ok=True)
    output_path = os.path.join('data', 'ethiopian_bank_reviews_raw.csv')
    df_all.to_csv(output_path, index=False)
    print(f"Saved raw reviews to {output_path}")

if __name__ == "__main__":
    main()
