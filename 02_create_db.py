import pandas as pd
import sqlite3

# Load the data we generated in Phase 1
df = pd.read_csv('dubai_cashless_2026_data.csv')

# Connect to (or create) the SQLite database
conn = sqlite3.connect('dubai_retail.db')

# Write the data to a table called 'transactions'
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Phase 2 Setup Complete: 'dubai_retail.db' created with 'transactions' table.")
conn.close()