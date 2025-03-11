import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('database.csv')

print(df.head())
print(df['Type'].unique())
print(df['Type'].nunique())
print(df['Type'].value_counts()['Strength'])
print((df['Type']=='Strength').sum())
print(df['Type'].count())
print(df['Equipment'].unique())
print(df['BodyPart'].unique())
print(df['Level'].unique())
print(df.loc[df['Level']=='Intermediate', 'Rating'].mean())
print(df['Rating'].mean())
print(df['Rating'].median())
print(df['Rating'].mode()[0])
print(df['Rating'].sum())
print(df['Rating'].min())
print(df['Rating'].max())

bar_level_label = np.array(['Beginner', 'Intermediate', 'Expert'])
bar_level_mean = np.array((df.loc[df['Level']=='Beginner', 'Rating'].mean(), df.loc[df['Level']=='Intermediate', 'Rating'].mean(), df.loc[df['Level']=='Expert', 'Rating'].mean()))

#Question: What is the average rating per Exercise Level?
plt.bar(bar_level_label, bar_level_mean)
plt.show()
