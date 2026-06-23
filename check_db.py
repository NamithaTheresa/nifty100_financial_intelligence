import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql(
    "SELECT COUNT(*) as total FROM companies",
    conn
)

print(df)

conn.close()