""" Topic:7. Series Indexing and Slicing """

import numpy as np
import pandas as pd


x = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])

#integer indexing
x[0]                #12
x[3]                #35

#slicing
print(x[5:9])

#negative slicing
print(x[-4 : ])
print(x[-5:])
print(x[: : 2])


#fancy indexing
print(x[[1, 3, 4, 6, 8]])


#indexing with labels -> fancy indexing
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
print(movies)
print(movies["Awara Paagal Deewana"])