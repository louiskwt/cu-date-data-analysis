import pandas as pd
from functools import reduce

df1 = pd.read_csv("csv/users.csv", sep=',')

df2 = pd.read_csv("csv/relationship.csv", sep=',')

df3 = pd.read_csv("csv/preference.csv", sep=',')

df4 = pd.read_csv('csv/merged-users.csv', sep=',')

# compile the list of dataframes


# Merging data_frames using reduce
output_one = pd.merge(df4, df3, on="name", how="inner")


# df_merged.to_csv('csv/mergedUsers.csv', index=False)
output_one.to_csv('csv/merged-all.csv', index=False)

print('Completed')
