import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")
profit_df = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

balance_df = pd.read_sql(
    "SELECT * FROM balancesheet",
    conn
)
df = pd.merge(
    profit_df,
    balance_df,
    on=["company_id", "year"]
)
df["equity"] = df["equity_capital"] + df["reserves"]
df["capital_employed"] = (
    df["total_assets"] -
    df["other_liabilities"]
)
df["NPM"] = df.apply(
    lambda row:
    None if row["sales"] == 0
    else (row["net_profit"] / row["sales"]) * 100,
    axis=1
)
df["OPM"] = df.apply(
    lambda row:
    None if row["sales"] == 0
    else (row["operating_profit"] / row["sales"]) * 100,
    axis=1
)
df["ROE"] = df.apply(
    lambda row:
    None if row["equity"] <= 0
    else (row["net_profit"] / row["equity"]) * 100,
    axis=1
)
df["ROCE"] = df.apply(
    lambda row:
    None if row["capital_employed"] <= 0
    else (
        row["operating_profit"] /
        row["capital_employed"]
    ) * 100,
    axis=1
)
df["OPM_Difference"] = (
    df["OPM"] -
    df["opm_percentage"]
)
print(df[
    [
        "company_id",
        "year",
        "NPM",
        "OPM",
        "ROE",
        "ROCE",
        "opm_percentage",
        "OPM_Difference"
    ]
].head(20))

df.to_csv(
    "reports/profitability_ratios.csv",
    index=False
)

print("profitability_ratios.csv generated successfully")