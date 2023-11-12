import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./data.csv")
data = data.iloc[::, 3::]

# checking which gender makes most transaction
dates = data[["Date", "Transaction Amount"]]
dates_column = pd.to_datetime(dates["Date"], format='mixed')
dates = dates.assign(Day=dates_column.dt.day, Month=dates_column.dt.month, Year=dates_column.dt.year)
dates = dates.drop("Date", axis=1)
dates["Day_Group"] = pd.cut(dates["Day"], [0,10,20,31], labels=["Start of month", "middle of month", "End of month"])

grouped_data = dates[["Day_Group", "Transaction Amount"]].groupby("Day_Group", observed=False).sum().reset_index()
plt.bar(x=grouped_data["Day_Group"], height=grouped_data["Transaction Amount"])
plt.show()