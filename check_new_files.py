import pandas as pd

files = [
    "stock_prices.xlsx",
    "financial_ratios.xlsx",
    "market_cap.xlsx",
    "peer_groups.xlsx",
    "sectors.xlsx"
]

for file in files:

    print("="*60)
    print(file)

    df = pd.read_excel(
        f"data/raw/{file}",
        header=0
    )

    print("Rows :", df.shape[0])
    print("Columns :", df.shape[1])
    print(df.columns.tolist())