import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")
print(df.head())

#graph 3

# Countplot
sns.countplot(x="sex", hue="target", data=df, palette="dark")

# Title and labels
plt.title("Heart Disease by Gender", fontsize=14)
plt.xlabel("Sex (0 = Female, 1 = Male)", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Legend
plt.legend(title="Heart Disease", labels=["No", "Yes"])

# Grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()
#------------------------------------------------------------------------

# graph 4
# countplot
sns.countplot(x="chest_pain_type", hue="target", data=df)

# add title
plt.title("Chest Pain Type vs Heart Disease")
plt.xlabel("Chest Pain Type")
plt.ylabel("Count")

# show the graph
plt.show()
#------------------------------------------------------------------------------

#graph 5
# add graph settings
sns.boxplot(x="target", y="cholestoral", data=df)
#add title
plt.title("Cholesterol vs Heart Disease")
plt.xlabel("Heart Disease")
plt.ylabel("Cholesterol")
#show graph
plt.show()