import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.reviews_utils import preprocess_reviews
import pandas as pd

def main():
    print("Starting preprocessing...")

    input_path = 'data/ethiopian_bank_reviews_raw.csv'
    output_path = 'data/ethiopian_bank_reviews_clean.csv'

    if not os.path.exists(input_path):
        print(f" File not found: {input_path}")
        return

    print("Reading raw data...")
    df_raw = pd.read_csv(input_path)
    print(f" Raw data shape: {df_raw.shape}")

    print("Preprocessing...")
    df_clean = preprocess_reviews(df_raw)
    print(f" Cleaned data shape: {df_clean.shape}")

    print("💾 Saving cleaned data...")
    df_clean.to_csv(output_path, index=False)
    print(f" Cleaned data saved to: {output_path}")


if __name__ == "__main__":
    main()
