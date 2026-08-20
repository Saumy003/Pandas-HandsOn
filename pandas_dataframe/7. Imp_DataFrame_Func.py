""" Topic: 7 Important DataFrame Functions -> astype """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

# astype
print(matches.info())
print(matches["ID"].astype("int32"))

matches["Season"] = matches["Season"].astype("category")
print(matches.info())