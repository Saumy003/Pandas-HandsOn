""" Topic 8. unique(series) """

import numpy as np
import pandas as pd

# unique -> provie array of unique element
temp = pd.Series([1, 1, 1, 1, 3, 4, 2, 1, 2, 3, np.nan, np.nan, 2, 3 ])
print(temp)
print(temp.unique())
print(len(temp.unique()))


# nunique(series + dataframe) --> not count missing values
matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")

print(matches["Season"].nunique())