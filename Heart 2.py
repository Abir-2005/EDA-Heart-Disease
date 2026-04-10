import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")
# to show the total output
print(df.head())

# graph 1
# Countplot for Heart Disease
sns.countplot(x="target", data=df)

# Add labels and title
plt.title("Distribution of Heart Disease")
plt.xlabel("Heart Disease (0 = No, 1 = Yes)")
plt.ylabel("Count")
# Show plot
plt.show()

#---------------------------------------------------------------------------
#graph 2

# Histogram for Heart Disease
plt.hist(df["age"], bins=30, color="skyblue", edgecolor="black")

# Bin = 30 means 30 smaller groups; More detailed view; Graph looks clear and smooth

# Add labels and title
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

#editing
plt.grid(axis='y', linestyle='--', alpha=0.7)

#plot show 
plt.show()
