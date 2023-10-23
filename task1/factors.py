import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('task1\spotify.csv', sep=',', encoding='latin-1')

data = data.drop(['bpm', 'key', 'mode'], axis=1)
data = data.dropna()

factors = data[["danceability_%","valence_%","energy_%","acousticness_%","instrumentalness_%","liveness_%","speechiness_%", "streams"]]

# Clean up the 'streams' column by keeping only numeric characters
factors.loc[:, 'streams'] = factors['streams'].replace({'[^0-9]': ''}, regex=True)

# Convert the 'streams' column to int64
factors.loc[:, 'streams'] = pd.to_numeric(factors['streams'], errors='coerce')

# Drop rows with NaN values in the 'streams' column (if any)
factors = factors.dropna(subset=['streams'])

# creating collection of all the different datasets onto which
# we will perform our analysis and visualizations
collection : pd.DataFrame = []
for col in factors.columns:
    collection.append(pd.DataFrame({col: factors[col], 'streams': factors['streams']}))

# removing the repeation
collection.pop()

max = []
min = []

for i in collection:
    max.append(i.iloc[:, 0].max())
    min.append(i.iloc[:, 0].min())
    
divisions = []
for i in range(0, 7):
    divisions.append(np.linspace(min[i], max[i], num=10))

labels = [10, 20, 30, 40, 50, 60, 70, 80, 90]

count = 0
result = []
for i in collection:
    i["category"] = pd.cut(i.iloc[:, 0], bins=divisions[count], labels=labels, include_lowest=True)
    count = count + 1
    result.append(i.groupby("category", observed = True).mean())

for i in result:
    i.plot(x=i.columns[0], y='streams', kind='bar')
    
plt.show()
