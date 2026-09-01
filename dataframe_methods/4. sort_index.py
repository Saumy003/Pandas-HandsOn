""" Topic 4. Sort_index """

import numpy as np
import pandas as pd

movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

marks = {
    "maths" : 97,
    "hindi" : 88,
    "science" : 93,
    "english" : 94
}

marks_series = pd.Series(marks)
print(marks_series)

# sort_index --> applied on series
print(marks_series.sort_index())


#sort_index  --> appiled on DataFrame
print(movies.sort_index(ascending=False))