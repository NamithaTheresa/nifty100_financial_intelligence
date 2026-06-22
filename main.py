import pandas as pd

from src.validators.schema_validator import *

all_failures = []


companies_df = pd.read_excel("data/raw/companies.xlsx", header=1)
all_failures.extend(validate_companies(companies_df))

profit_df = pd.read_excel("data/raw/profitandloss.xlsx", header=1)
all_failures.extend(validate_profitandloss(profit_df))

balance_df = pd.read_excel("data/raw/balancesheet.xlsx", header=1)
all_failures.extend(validate_balancesheet(balance_df))

cashflow_df = pd.read_excel("data/raw/cashflow.xlsx", header=1)
all_failures.extend(validate_cashflow(cashflow_df))

analysis_df = pd.read_excel("data/raw/analysis.xlsx", header=1)
all_failures.extend(validate_analysis(analysis_df))

documents_df = pd.read_excel("data/raw/documents.xlsx", header=1)
all_failures.extend(validate_documents(documents_df))

proscons_df = pd.read_excel("data/raw/prosandcons.xlsx", header=1)
all_failures.extend(validate_prosandcons(proscons_df))


failure_df = pd.DataFrame(
    all_failures,
    columns=[
        "dataset",
        "row_number",
        "error"
    ]
)

failure_df.to_csv(
    "validation_failures.csv",
    index=False
)

print(f"Total Validation Failures: {len(all_failures)}")
print("validation_failures.csv generated successfully")