""" Topic 9. WORKING WITH MISSING VALUES """

import numpy as np
import pandas as pd

# 1. isnull() or notnull() use to check missing values.
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")
print(movies.isnull())


# 2. dropna(series + dataframe) -> a complete row will me removed if one missing value will be present.
print(movies)
print(movies.dropna())
print(movies.dropna(how="all"))                    # how parameter => give instruction what to remove!
print(movies.dropna(subset=["wins_nominations"]))  # subset parameter => remove all row jis me win_nomination missing ho!


# 3. fillna(series + dataframes) -> fill NaN with Don't Know or anything you want.
print(movies.fillna("Don't Know"))