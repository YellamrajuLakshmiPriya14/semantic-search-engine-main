import duckdb
import pandas as pd
import re

# Connect to database
conn = duckdb.connect("data/support.duckdb")

# Read raw_data table
df = conn.execute("""
SELECT * FROM raw_data
""").fetchdf()

print("Rows loaded:", len(df))

# Cleaning function
def clean_text(text):

    if pd.isna(text):
        return ""

    text = str(text)

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

    # Convert to lowercase
    text = text.lower()

    return text

# Apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned data
conn.execute("""
CREATE OR REPLACE TABLE processed_data AS
SELECT * FROM df
""")

print("Cleaning completed!")