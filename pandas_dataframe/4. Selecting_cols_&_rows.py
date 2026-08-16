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


""" Topic:4 Selecting ROWS from a DataFrame """

student_dict = {
    "name" : ["nitish", "rahul", "rishab", "karan"],
    "iq" : [100, 90, 120, 80],
    "marks" : [80, 70, 100, 50],
    "package": [10, 7, 14, 2]
}

student_info = pd.DataFrame(student_dict)

student_info.set_index("name", inplace=True)
print(student_info)

#iloc --> searches using index position

#select single row
print(movies.iloc[0 : 11 : 2])

#fancy indexing
print(movies.iloc[[0, 4, 5]])

#loc --> searches usimg index lables

#select single row
print(student_info.loc["rahul"])

#select multiple rows
print(student_info.loc["nitish" : "karan"])
print(student_info.loc[["nitish", "rishab", "rahul"]])


""" Topic: 4 Selecting both rows and cols  """

print(movies.iloc[0:3, 0:3])

print(movies.loc[0:3, "title_x" : "poster_path"])