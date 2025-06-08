import pandas as pd
import cx_Oracle

def main():
    # Load CSV file
    csv_path = "../data/ethiopian_bank_reviews_clean.csv"  
    df = pd.read_csv(csv_path)

    # Oracle DB connection setup
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
    connection = cx_Oracle.connect(user="bank_reviews", password="bank_password", dsn=dsn)
    cursor = connection.cursor()

    try:
        # Insert unique banks and get their IDs
        banks = df["bank"].unique()
        bank_ids = {}

        for bank in banks:
            id_var = cursor.var(int)
            cursor.execute(
                "INSERT INTO banks (name) VALUES (:1) RETURNING id INTO :2",
                (bank, id_var)
            )
            bank_ids[bank] = id_var.getvalue()[0]

        # Insert reviews linked to banks
        for _, row in df.iterrows():
            bank_id = bank_ids[row["bank"]]
            cursor.execute("""
                INSERT INTO reviews (review_text, rating, review_date, bank_id, source)
                VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5)
            """, (row["review"], row["rating"], row["date"], bank_id, row["source"]))

        # Commit the transaction
        connection.commit()
        print("Data loaded successfully!")

    except cx_Oracle.DatabaseError as e:
        print(f"Database error occurred: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
