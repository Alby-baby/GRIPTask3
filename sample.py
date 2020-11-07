import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sample=pd.read_csv('Downloads\SampleSuperstore.csv')
sample.head()
sample.describe()
sample.info()
sample.isnull().sum()

sample.duplicated().sum()

sample.drop_duplicates(inplace=True)

sns.heatmap(sample.corr(), cmap = "Reds")

sns.pairplot(sample)
plt.figure(figsize = (20, 10))
sns.countplot(x = 'Sub-Category', hue = 'Region', data =sample,palette = 'twilight') 

#classification according to region
plt.figure(figsize = (20, 10))
sns.countplot(x = 'Category', hue = 'Region', data = sample, palette = 'twilight')

#quantities ordered vs state
plt.figure(figsize = (10, 6))
sns.countplot(x = sample['State'], palette = 'twilight_shifted', order = (sample['State'].value_counts().head(25)).index)

plt.figure(figsize=(15,8))
sns.scatterplot(sample['Sub-Category'], sample['Profit'])
plt.figure(figsize=(15,8))
sns.scatterplot(sample['Sub-Category'], sample['Profit'])

plt.figure(figsize=(15,8))
sns.barplot(sample['Sub-Category'], sample['Profit'])
plt.figure(figsize=(15,8))
sns.barplot(sample['Category'], sample['Profit'])

