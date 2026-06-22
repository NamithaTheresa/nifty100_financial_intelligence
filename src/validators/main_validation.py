import pandas as pd

from src.validators.schema_validator import validate_profitandloss


df = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

failures = validate_profitandloss(df)

print(failures)