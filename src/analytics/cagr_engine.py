import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql(
    """
    SELECT company_id,
           year,
           sales,
           net_profit,
           eps
    FROM profitandloss
    """,
    conn
)

conn.close()
df["year_num"] = (
    df["year"]
    .astype(str)
    .str.extract(r"(\d{4})")[0]
)

df["year_num"] = pd.to_numeric(
    df["year_num"],
    errors="coerce"
)

df = df.dropna(subset=["year_num"])

df["year_num"] = df["year_num"].astype(int)

df = df.sort_values(["company_id", "year_num"])
def calculate_cagr(start_value, end_value, years):

    if (
        start_value <= 0
        or end_value <= 0
        or years <= 0
    ):
        return None

    return (
        ((end_value/start_value)**(1/years)-1)
        *100
    )
results=[]
for company in df["company_id"].unique():

    company_df = df[
        df["company_id"] == company
    ].reset_index(drop=True)

    revenue3 = revenue5 = revenue10 = None
    pat3 = pat5 = pat10 = None
    eps3 = eps5 = eps10 = None

    turnaround = False
    # 3-Year CAGR
    if len(company_df) >= 4:

        start = company_df.iloc[-4]
        end = company_df.iloc[-1]

        revenue3 = calculate_cagr(
            start["sales"],
            end["sales"],
            3
        )
        pat3 = calculate_cagr(
    start["net_profit"],
    end["net_profit"],
    3
)

        eps3 = calculate_cagr(
    start["eps"],
    end["eps"],
    3
)
        print("================================")
        print(company)
        print(company_df[["year", "sales"]].tail(4))
        print("Start:", start["sales"])
        print("End:", end["sales"])
        print("Revenue3:", revenue3)
    if len(company_df)>=6:

        start=company_df.iloc[-6]

        end=company_df.iloc[-1]

        revenue5=calculate_cagr(
            start["sales"],
            end["sales"],
            5
        )

        pat5=calculate_cagr(
            start["net_profit"],
            end["net_profit"],
            5
        )

        eps5=calculate_cagr(
            start["eps"],
            end["eps"],
            5
        )
        


    if len(company_df)>=11:

        start=company_df.iloc[-11]

        end=company_df.iloc[-1]

        revenue10=calculate_cagr(
            start["sales"],
            end["sales"],
            10
        )

        pat10=calculate_cagr(
            start["net_profit"],
            end["net_profit"],
            10
        )

        eps10=calculate_cagr(
            start["eps"],
            end["eps"],
            10
        )
    turnaround=True
    turnaround=False

    if (
        company_df.iloc[0]["net_profit"]<0
        and
        company_df.iloc[-1]["net_profit"]>0
    ):
        turnaround=True
        print(
    company,
    revenue3,
    revenue5,
    revenue10
)
    results.append({

        "company_id":company,

        "Revenue_CAGR_3Y":revenue3,

        "Revenue_CAGR_5Y":revenue5,

        "Revenue_CAGR_10Y":revenue10,

        "PAT_CAGR_3Y":pat3,

        "PAT_CAGR_5Y":pat5,

        "PAT_CAGR_10Y":pat10,

        "EPS_CAGR_3Y":eps3,

        "EPS_CAGR_5Y":eps5,

        "EPS_CAGR_10Y":eps10,

        "Turnaround":turnaround

    })
result_df=pd.DataFrame(results)

result_df.to_csv(

    "reports/cagr_engine.csv",

    index=False

)

print(result_df.head(10))
