""" Topic:4 Selecting COLS from a DataFrame """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

#fetch single col
print(movies["title_x"])
print(matches["City"])

#fetche multiple cols
print(movies[["title_x", "year_of_release", "actors"]])
print(matches[["Team1", "Team2", "WinningTeam"]])


""" Selecting ROWS from a DataFrame """

student_dict = {
    "name" : ["nitish", "rahul", "rishab", "karan"],
    "iq" : [100, 90, 120, 80],
    "marks" : [80, 70, 100, 50],
    "package": [10, 7, 14, 2]
}

student_info = pd.DataFrame(student_dict)

student_info.set_index("name", inplace=True)
print(student_info)

#select single row

