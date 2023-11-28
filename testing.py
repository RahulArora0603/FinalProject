import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bmi.csv')

x = df['Age'].value_counts()
y = df['Age'].value_counts().keys()
plt.bar(y ,x , color ="black")
plt.show()