""" Topic 11. drop() ->(series + dataframes) """

import numpy as np
import pandas as pd

# in Series
temp = pd.Series([1, 1, 1, 1, 3, 4, 2, 1, 2, 3, np.nan, np.nan, 2, 3 ])
print(temp.drop(index=[1, 6]))   #--> drop is use to delete row or column

# in Dataframes
matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
print(matches.drop(columns=['ID', 'City']))   # delete entire ID and City column.