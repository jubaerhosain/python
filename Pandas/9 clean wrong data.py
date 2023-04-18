import pandas as pd

df = pd.read_csv('data/data2.csv')

print(df.to_string())

# for i in df.index:
#     if df.loc[i, 'Duration'] > 120:
#         df.loc[i, 'Duration'] = 120

# print(df.to_string())

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
        
print(df.to_string())
