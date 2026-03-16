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
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')


df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Infinity handle---
df = df.replace([np.inf, -np.inf], np.nan)
                
df = df.fillna(0) 

# --- CLEANING END ---

print("\nAfter cleaning, missing values:")
print(df.isnull().sum())

df.to_csv('cleaned_indian_employee_Data.csv', index=False)
print('\nData cleaning completed! Saved successfully.')