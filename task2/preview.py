import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('task2\Iris.csv', sep=',', encoding='latin-1')

median = data[data.columns[1:5]].median()
mode = data[data.columns[1:5]].mode()
mean = data[data.columns[1:5]].mean()
standard_deviation = data[data.columns[1:5]].std()
correlation_coefficient = data[data.columns[1:5]].corr()

sepal_length = pd.DataFrame(data.groupby("SepalLengthCm", observed=True).count()["Id"]).sort_values(by=["Id"], ascending=False)

species = pd.DataFrame(data.groupby("Species").mean()).iloc[0::, 1::]
species.reset_index(inplace=True)


plt.scatter(data["SepalLengthCm"], data["PetalWidthCm"], label="Data Points")


model = LinearRegression()
x = data[["SepalLengthCm"]]
y = data["PetalWidthCm"]
model.fit(x, y)

plt.plot(data['SepalLengthCm'], model.predict(x), color='green', label='Linear Regression')

plt.show()


