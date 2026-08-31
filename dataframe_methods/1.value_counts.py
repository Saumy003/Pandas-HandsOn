""" Topic 1. Value Counts """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")

# value_counts --> Series
a = pd.Series([1, 1, 1, 1, 2, 2, 2, 3])
count_freq = a.value_counts()
print(count_freq)


# value_counts --> DataFrame
student_details = [
    [80, 70, 14],
    [90, 70, 7],
    [100, 80, 10],
    [120, 100, 14],
    [90, 70, 7]
]

lst = pd.DataFrame(student_details, columns= ["iq", "marks", "package"])
freq_of_rows = lst.value_counts()
print(freq_of_rows)


# find which player has won most potm -> in finals & qualifiers
final_qualifiers = ~matches["MatchNumber"].str.isdigit()
print(matches[final_qualifiers]["Player_of_Match"].value_counts())

# toss decision plot
print(matches["TossDecision"].value_counts().plot(kind="pie"))
plt.show()

# how many matches each team has played
print((matches["Team1"].value_counts() + matches["Team2"].value_counts()).sort_values(ascending=False))