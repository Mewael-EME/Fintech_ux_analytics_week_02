# Ethiopian Bank App Reviews Analysis

This project analyzes Google Play Store reviews for:

- Commercial Bank of Ethiopia  
- Bank of Abyssinia  
- Dashen Bank  
- Awash Bank  

## Methodology

### 1. Web Scraping  
- Collected reviews using `google-play-scraper` for Commercial Bank of Ethiopia, Dashen Bank, and Bank of Abyssinia  
- Extracted fields: review text, rating, date, bank name, source  

### 2. Data Preprocessing  
- Removed duplicates and irrelevant content  
- Filtered out emojis and non-standard characters  
- Normalized dates to `YYYY-MM-DD`  
- Saved cleaned data as CSV with: review, rating, date, bank, source  

### 3. Store Cleaned Data in Oracle  
- Designed and implemented a relational database in Oracle XE (Express Edition)  
- Created a database named `bank_reviews`  
- Defined schema with:  
  - **Banks Table:** stores bank information  
  - **Reviews Table:** stores cleaned review data  
- Inserted cleaned reviews into Oracle DB using Python scripts  
- PostgreSQL fallback option available if Oracle XE setup issues occur  

### 4. Topic Modeling  
- Applied LDA (Gensim) with tokenization and stopword removal  
- Generated 5 main topics to uncover recurring themes  
- Complements rule-based theme mapping  

### 5. Sentiment Analysis  
- Classified reviews as positive, neutral, or negative  
- Analyzed sentiment trends per bank  

### 6. Visualization  
- Created plots for review volume, sentiment distribution, and theme frequency  
- Saved per-bank theme counts in `themes_per_bank.csv`  

## Tools

- Python (pandas, numpy)  
- google-play-scraper  
- Gensim  
- NLTK / spaCy  
- Matplotlib, Seaborn, Plotly  
- Oracle XE (or PostgreSQL fallback)  
- Git + GitHub  

## Usage

Run `task2_analysis.py` to:  
- Print top LDA topics  
- Save theme counts per bank  

## Future Work

- Expand data sources to App Store and social media  
- Improve sentiment analysis with custom fine-tuned models  
- Develop real-time dashboards for user feedback monitoring  
