# Ethiopian Bank App Reviews Analysis

This project collects and analyzes Google Play Store reviews for:
- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank
- Awash Bank

## Methodology

### 1. Web Scraping
- Collected reviews from Google Play Store for:
  - Commercial Bank of Ethiopia
  - Dashen Bank
  - Bank of Abyssinia
- Collected fields: review text, rating, date, bank name, source.

### 2. Data Preprocessing
- Removed duplicate reviews
- Dropped rows with missing or junk content
- Filtered out reviews with emojis or non-standard characters
- Normalized dates to `YYYY-MM-DD` format
- Final output saved as a clean CSV with:
  - `review`, `rating`, `date`, `bank`, `source`


## Tools
- Python, pandas
- google-play-scraper
- Git + GitHub
"# Fintech_ux_analytics_week_02" 
