import pandas as pd
import sqlite3

#상의
df = pd.read_csv('clean.csv')

conn = sqlite3.connect('clothes.db')

table_name = 'clothes'
df.to_sql(table_name, conn)

conn.close()