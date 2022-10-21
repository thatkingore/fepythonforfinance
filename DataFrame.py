# Using Pandas

import pandas as pd

# Importing a .csv file

sp500_companies = pd.read_csv("/Users/oredaodu/Documents/edu/FE/1/Python/S&P500Companies.csv")
print(sp500_companies.head())

sp500_short = sp500_companies[['Name', 'x1st.day', 'x2nd.day', 'x3rd.day', 'x4th.day', 'x5th.day']]
print(sp500_short.head())

sp500_short.columns = ['Name', '1st Day', '2nd Day', '3rd Day', '4th Day', '5th Day']
print(sp500_short.head())

sp500 = pd.read_csv("/Users/oredaodu/Documents/edu/FE/1/Python/S&P500.csv", index_col=0)
print(sp500.head())

print(sp500.index)
print(sp500.loc['11/8/2019'])

print(sp500.info())
print(type(sp500))
print(len(sp500))
print(sp500.columns)

print(sp500.High['11/11/2019'])
print(sp500.loc['11/11/2019', 'High'])

df1 = pd.DataFrame(
    {"a" : [1, 2, 3],
     "b" : [4, 5, 6]},
    index = [1, 2, 3]
)

df2 = pd.DataFrame(
    {"a" : [1, 2, 4],
     "b" : [7, 8, 9]},
    index = [1, 2, 3]
)

print(df1)
print(df2)

print(pd.merge(df1, df2, how='left', on='a'))
print(pd.merge(df1, df2, how='right', on='a'))
print(pd.merge(df1, df2, how='inner', on='a'))
print(pd.merge(df1, df2, how='outer', on='a'))
