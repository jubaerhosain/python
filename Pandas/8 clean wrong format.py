import pandas as pd

df = pd.read_csv('data/data2.csv')
# print(df.to_string())

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace=True)


print(df.to_string())
