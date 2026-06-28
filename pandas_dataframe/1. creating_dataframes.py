""" Topic 1: Creating DataFrame """

import numpy as np
import pandas as pd

# using list (2d list)
student_data = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

list_to_dataframe = pd.DataFrame(student_data, columns=["iq", "marks", "package"])
print(list_to_dataframe)


#using dict
student_dict = {
    "iq" : [100, 90, 120, 80],
    "marks" : [80, 70, 100, 50],
    "package": [10, 7, 14, 2]
}

dataframe_using_dict = pd.DataFrame(student_dict)
print(dataframe_using_dict)


#using read_csv
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")
print(movies)

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
print(matches)