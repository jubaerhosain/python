import pandas as pd

df = pd.read_csv('data/data2.csv')

print(df.to_string())

print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df.to_string())

