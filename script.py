import pandas as pd

df1 = pd.read_csv("user.csv")

df2 = pd.read_csv("relationship.csv")

print(df2)

# output = pd.merge(df1, df2, on="name", how="inner")


# print(output)

# output.to_csv("merged.csv", index=False)

# print('completed')
