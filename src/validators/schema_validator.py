import pandas as pd


def validate_companies(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_name"]):
            failures.append(["companies", index, "company_name is null"])

        if pd.isna(row["website"]):
            failures.append(["companies", index, "website is null"])

    return failures


def validate_profitandloss(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["profitandloss", index, "company_id is null"])

        if row["sales"] <= 0:
            failures.append(["profitandloss", index, "sales <= 0"])

        if pd.isna(row["net_profit"]):
            failures.append(["profitandloss", index, "net_profit is null"])

    return failures


def validate_balancesheet(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["balancesheet", index, "company_id is null"])

        if row["total_assets"] <= 0:
            failures.append(["balancesheet", index, "total_assets <= 0"])

        if row["total_liabilities"] <= 0:
            failures.append(["balancesheet", index, "total_liabilities <= 0"])

    return failures


def validate_cashflow(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["cashflow", index, "company_id is null"])

        if pd.isna(row["net_cash_flow"]):
            failures.append(["cashflow", index, "net_cash_flow is null"])

    return failures


def validate_analysis(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["analysis", index, "company_id is null"])

        if pd.isna(row["roe"]):
            failures.append(["analysis", index, "roe is null"])

    return failures


def validate_documents(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["documents", index, "company_id is null"])

        if pd.isna(row["Annual_Report"]):
            failures.append(["documents", index, "Annual_Report is null"])

    return failures


def validate_prosandcons(df):
    failures = []

    for index, row in df.iterrows():

        if pd.isna(row["company_id"]):
            failures.append(["prosandcons", index, "company_id is null"])

        if pd.isna(row["pros"]):
            failures.append(["prosandcons", index, "pros is null"])

        if pd.isna(row["cons"]):
            failures.append(["prosandcons", index, "cons is null"])

    return failures