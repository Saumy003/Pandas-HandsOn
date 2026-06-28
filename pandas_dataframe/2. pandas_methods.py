""" Topic 2: Pandas Attributes and Methods """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")


# shape
print(movies.shape)
print(matches.shape)

# dtypes
print(movies.dtypes)

# index
print(matches.index)
print(movies.index)

# column
print(movies.columns)
print(matches.columns)

# values
print(matches.values)


""" Methods """

# head and tail
print(movies.head())
print(matches.tail(2))

# sample
print(matches.sample())

# info
print(movies.info())
print(matches.info())

# describe
print(movies.describe())
print(matches.describe())

# isnull
print(movies.isnull())
print(movies.isnull().sum())
print(matches.isnull())

# duplicated
print(movies.duplicated())
print(movies.duplicated().sum())

# rename
print(movies.rename(columns={"title_x" : "title_z"}))
