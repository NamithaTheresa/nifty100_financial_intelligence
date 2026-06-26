import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

profit_df = pd.read_sql("SELECT * FROM profitandloss", conn)
balance_df = pd.read_sql("SELECT * FROM balancesheet", conn)

conn.close()
df = pd.merge(
    profit_df,
    balance_df,
    on=["company_id", "year"]
)
df["equity"] = df["equity_capital"] + df["reserves"]
BANK_KEYWORDS = [
    "BANK",
    "HDFCBANK",
    "ICICIBANK",
    "SBIN",
    "AXISBANK",
    "KOTAKBANK",
    "INDUSINDBK",
    "BANKBARODA"
]
def calculate_de(row):

    if any(bank in row["company_id"] for bank in BANK_KEYWORDS):
        return None

    if row["equity"] <= 0:
        return None

    return row["borrowings"] / row["equity"]
def calculate_icr(row):

    if row["interest"] == 0:
        return None

    return row["operating_profit"] / row["interest"]
def calculate_asset_turnover(row):

    if row["total_assets"] == 0:
        return None

    return row["sales"] / row["total_assets"]
df["Debt_to_Equity"] = df.apply(calculate_de, axis=1)

df["Interest_Coverage"] = df.apply(calculate_icr, axis=1)

df["Asset_Turnover"] = df.apply(
    calculate_asset_turnover,
    axis=1
)
df.to_csv(
    "reports/leverage_efficiency_ratios.csv",
    index=False
)

print("Leverage & Efficiency ratios generated.")
