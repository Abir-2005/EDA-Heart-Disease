import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/abirp/OneDrive/文档/Edge Computing Book Chapter/Heart Disease/HeartDiseaseTrain-Test.csv.xlsx")
print(df.head())

# graph 6
sns.set_style("whitegrid")

#add graph data
sns.violinplot(x="target", y="resting_blood_pressure", data=df, palette="dark")

#add title
plt.title("Resting Blood Pressure Distribution vs Heart Disease", fontsize=14)
plt.xlabel("Heart Disease (0 = No, 1 = Yes)", fontsize=12)
plt.ylabel("Resting Blood Pressure", fontsize=12)

#plot show
plt.show()

#--------------------------------------------------------------------------------------
# graph 7
sns.kdeplot(data=df, x="Max_heart_rate", hue="target", fill=True)

#add title
plt.title("Density of Max Heart Rate by Heart Disease", fontsize=14)
plt.xlabel("Max Heart Rate", fontsize=12)
plt.ylabel("Density", fontsize=12)

#plot show
plt.show()

