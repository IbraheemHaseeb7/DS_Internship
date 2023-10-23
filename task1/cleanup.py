import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('task1\spotify.csv', sep=',', encoding='latin-1')

print(data)
