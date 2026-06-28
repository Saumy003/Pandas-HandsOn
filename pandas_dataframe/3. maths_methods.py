""" Topic:3 Mathematical Methods """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")
student_data = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]
students = pd.DataFrame(student_data)


# sum
print(movies.sum())
print(students.sum(axis=1))

# mean
print(students.mean())

# min & max
print(matches.max())
print(students.min())

# std & var
print(movies.std())
print(students.var())