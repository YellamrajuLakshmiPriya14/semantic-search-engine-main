import pandas as pd
import duckdb

# Read CSV
df = pd.read_csv("data/twcs.csv")

# Show first 5 rows
print(df.head())

# Connect to DuckDB
conn = duckdb.connect("data/support.duckdb")

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS raw_data AS
SELECT * FROM df
""")

print("Data loaded successfully!")