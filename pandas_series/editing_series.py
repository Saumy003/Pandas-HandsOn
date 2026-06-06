""" Topic:8. Editing Series """

import numpy as np
import pandas as pd


#using indexing
x = pd.Series([10, 24, 33, 42, 55, 60, 76, 85, 78, 66])
x[4] = 100                             #--> change index 4 values to 100
print(x)

# what if an index does not exist
x["run"] = 21
print(x)


# using slicing
x[8 : 11]  = 42
print(x)


# using fancy indexing
x[[0, 6, 7]] = [87, 32, 90]
print(x)

# using index labels
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
movies["Awara Paagal Deewana"] = "Sunil Sheety"
print(movies)