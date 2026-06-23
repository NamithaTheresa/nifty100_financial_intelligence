import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

files = {
    "companies": "companies.xlsx",
    "profitandloss": "profitandloss.xlsx",
    "balancesheet": "balancesheet.xlsx",
    "cashflow": "cashflow.xlsx",
    "analysis": "analysis.xlsx",
    "documents": "documents.xlsx",
    "prosandcons": "prosandcons.xlsx"
}

for table_name, file_name in files.items():

    df = pd.read_excel(
        f"data/raw/{file_name}",
        header=1
    )

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully")

conn.close()

print("All datasets loaded into SQLite")