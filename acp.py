import pandas as pd
import numpy as np

data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', None, None, None],
    'Salary': [100, 200, None, None]
}

df = pd.DataFrame(data)

print("=== Original DataFrame ===")
print(df)

print("\n=== First 2 rows ===")
print(df.head(2))

print("\n=== Last 2 rows ===")
print(df.tail(2))

print("\n=== Total Null Values ===")
print(df.isnull().sum().sum())

print("\n=== DataFrame Info ===")
print(df.info())

df_rows_dropped = df.dropna()
print("\n=== DataFrame after dropping rows with nulls ===")
print(df_rows_dropped)

df_cols_dropped = df.dropna(axis=1)
print("\n=== DataFrame after dropping columns with nulls ===")
print(df_cols_dropped)

df_salary_filled = df.copy()
df_salary_filled['Salary'] = df_salary_filled['Salary'].fillna(300)
print("\n=== DataFrame after filling Salary nulls with 300 ===")
print(df_salary_filled)

df_role_filled = df.copy()
df_role_filled['Role'] = df_role_filled['Role'].fillna('CEO')
print("\n=== DataFrame after filling Role nulls with 'CEO' ===")
print(df_role_filled)