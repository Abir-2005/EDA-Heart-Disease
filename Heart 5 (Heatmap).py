import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")
print(df.head())

# graph 8
plt.figure(figsize=(10,8))

# add value
numeric_df = df.select_dtypes(include = ['int64','float64'])

# heatmap 
sns.heatmap(numeric_df.corr(), annot=True)

# title
plt.title("Feature Correlation Heatmap")

# plot show 
plt.show()

