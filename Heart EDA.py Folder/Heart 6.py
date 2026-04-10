import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")
print(df.head())

#graph 9
g = sns.FacetGrid(df, col="target")

g.map(sns.countplot, "thalassemia", palette="dark")

#plot show 
plt.show()

#-----------------------------------------------------------
# graph 10
# plot create
sns.scatterplot(
    x="cholestoral",
    y="Max_heart_rate",
    hue="target",
    size="age",
    data=df,
    alpha=0.7
)

# plot title 
plt.title("Cholesterol vs Max Heart Rate", fontsize=14)
plt.xlabel("Cholesterol Level", fontsize=12)
plt.ylabel("Max Heart Rate", fontsize=12)

# add legend
plt.legend(title="Heart Disease", labels=["No", "Yes"])

# add grids
plt.grid(True, linestyle='--', alpha=0.5)

# show thw graph
plt.show()