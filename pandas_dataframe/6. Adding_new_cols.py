""" Topic: 6 Adding New Cols """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

# adding new cols -> completely new col

movies["Country"] = "India"
print(movies.head(3))


# adding new cols --> from existing ones

