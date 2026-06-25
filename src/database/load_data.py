import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("nifty100.db")

# Dictionary of table names and file names
files = {
    "companies": "companies.xlsx",
    "profitandloss": "profitandloss.xlsx",
    "balancesheet": "balancesheet.xlsx",
    "cashflow": "cashflow.xlsx",
    "analysis": "analysis.xlsx",
    "documents": "documents.xlsx",
    "prosandcons": "prosandcons.xlsx",
    "stock_prices": "stock_prices.xlsx",
    "financial_ratios": "financial_ratios.xlsx",
    "market_cap": "market_cap.xlsx",
    "peer_groups": "peer_groups.xlsx",
    "sectors": "sectors.xlsx"
}

audit = []

for table_name, file_name in files.items():

    try:

        # Supplementary files use header=0
        if table_name in [
            "stock_prices",
            "financial_ratios",
            "market_cap",
            "peer_groups",
            "sectors"
        ]:
            header = 0
        else:
            header = 1

        df = pd.read_excel(
            f"data/raw/{file_name}",
            header=header
        )

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        audit.append([
            file_name,
            table_name,
            len(df),
            "Success"
        ])

        print(f"✓ {table_name} loaded successfully")

    except Exception as e:

        audit.append([
            file_name,
            table_name,
            0,
            f"Failed - {str(e)}"
        ])

        print(f"✗ Error loading {table_name}")
        print(e)

# Create audit DataFrame
audit_df = pd.DataFrame(
    audit,
    columns=[
        "file_name",
        "table_name",
        "rows_loaded",
        "status"
    ]
)

audit_df.to_csv(
    "load_audit.csv",
    index=False
)

conn.close()

print("\nAll loading completed.")
print("load_audit.csv generated successfully.")