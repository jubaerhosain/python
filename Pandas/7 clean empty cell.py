import pandas as pd

df = pd.read_csv('data/data2.csv')


# print(df.to_string())
# print(df.shape)

# new_df = df.dropna()

# print(new_df.to_string())
# print(new_df.shape)


# df.dropna(inplace=True)

# print(df.to_string())
# print(df.shape)


# df = pd.read_csv('data/data2.csv')

# df.fillna(130, inplace = True)
# print(df.to_string())
# print(df.shape)

# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())
# print(df.shape)

# x = df["Calories"].mean()
# x = df["Calories"].median()
x = df["Calories"].mode()[0]

print(df.info())

df["Calories"].fillna(x, inplace=True)
print(df.to_string())
