import pandas as pd
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== RANDOM SAMPLE =====")
print(df.sample(5))

print("\n===== DATASET SHAPE =====")
print("Rows, Columns:", df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== DATA INFORMATION =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== UNIQUE VALUES =====")
print(df.nunique())