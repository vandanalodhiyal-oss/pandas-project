#importing necessary libraries

import pandas as pd
import numpy as np

#loding the dataset

df = pd.read_csv("missing values check/_employe.csv - Sheet1 (3).csv")
print(df.head())

#checking the missing values
# Missing values check karne ke liye 
print('Missing values in each column:')
print(df.isnull().sum())


# --- CLEANING START ---

df['Salary'] = df['Salary'].astype(str).str.replace(',', '', regex=True)

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')


df.replace([np.inf, -np.inf], np.nan, inplace=True)

#  NaN values  (Fillna)
salary_mean = df['Salary'].mean()
age_mean = df['Age'].mean()

df['Salary'] = df['Salary'].fillna(salary_mean)
df['Age'] = df['Age'].fillna(age_mean)

df['Contact'] = df['Contact'].fillna(0)
df['City'] = df['City'].fillna('Unknown')

# --- CLEANING END ---

# Result check-----
print("Missing values after cleaning:")
print(df.isnull().sum())

# Final file save----
df.to_csv('cleaned_employee_data.csv', index=False)
print("\nSuccess! Data clean ho gaya aur 'cleaned_employee_data.csv' save ho gayi.")