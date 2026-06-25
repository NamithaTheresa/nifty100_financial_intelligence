import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

companies = [
    "ABB",
    "HDFCBANK",
    "INFY",
    "TCS",
    "RELIANCE"
]

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "financial_ratios",
    "market_cap",
    "stock_prices"
]

for company in companies:

    print("\n" + "=" * 60)
    print("Company:", company)

    for table in tables:

        query = f"""
        SELECT *
        FROM {table}
        WHERE company_id='{company}'
        LIMIT 5
        """

        df = pd.read_sql(query, conn)

        print(f"\nTable : {table}")
        print(df)

conn.close()