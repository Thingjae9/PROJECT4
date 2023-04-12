import pandas as pd
import sqlite3
import re

conn = sqlite3.connect('result.db')
df = pd.read_csv('csv/result.csv')
df['의류명'] = df['의류명'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
df.drop(['Unnamed: 0'],axis=1, inplace=True)
df.rename(columns = {'브랜드명':'brand'}, inplace=True)
df.rename(columns = {'의류명':'name'}, inplace=True)
df.rename(columns = {'성별':'gender'}, inplace=True)

df.to_csv('clean.csv')