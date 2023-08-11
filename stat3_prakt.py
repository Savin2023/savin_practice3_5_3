import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data=pd.read_csv("final_data.csv")
data.head(5)

print(data.columns) # 05.50 и перезаписываем только несколько полей
data=data[['bathrooms','bedrooms','finishedsqft', 'lastsoldprice', 
       'zestimate']].corr()
print(data)

plt.figure(figsize=(8,6))
sns.heatmap(data.corr())
plt.show()
