""" Topic:4. Creating Series Using read_csv """

import numpy as np
import pandas as pd


#with one col
pd.read_csv("D:\PANDAS\pandas_series\subs.csv")
print(type(pd.read_csv("D:\PANDAS\pandas_series\subs.csv")))                        #<class 'pandas.DataFrame'>
print(type(pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()))              #<class 'pandas.Series'>


#with 2 col
pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()

print(pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze())