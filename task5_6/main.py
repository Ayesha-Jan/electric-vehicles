import pandas as pd

# load your two datasets
df1 = pd.read_csv("data/ev_sales.csv")
df2 = pd.read_csv("data/energy_emissions.csv") 

df1.columns = df1.columns.str.strip()

print([repr(c) for c in df1.columns])

print(df1.head())
print(df1.columns)
print(df1.isnull().sum())

print(df2.head())
print(df2.columns)
print(df2.isnull().sum())

df1['country'] = df1['Entity'].str.strip().str.lower()
df2['country'] = df2['country'].str.strip().str.lower()

df1['Year'] = df1['Year'].astype(int)
df2['Year'] = df2['Year'].astype(int)

df1 = df1.drop(columns=['Entity', 'Code'])

merged_df = pd.merge(df1, df2, on=['country', 'Year'], how="outer")
merged_df.to_csv("merged_data.csv", index=False)
