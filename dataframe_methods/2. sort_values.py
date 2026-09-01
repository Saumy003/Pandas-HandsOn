""" Topic 2. Sort Values """

import numpy as np
import pandas as pd

movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

# sort_values --> Series
a = pd.Series([45, 68, 2, 35, 89, 22])
print(a)
print(a.sort_values())
print(a.sort_values(ascending=False))


# sort_values --> DataFrame
print(movies)
print(movies.sort_values("title_x"))
print(movies.sort_values("imdb_id"))
print(movies.sort_values("wins_nominations"))  #sort_values applied on missing values(NaN)

# apply sorting in multiple column in a single line of code:-
print(movies.sort_values(["year_of_release", "title_x"]))

print(movies.sort_values(["year_of_release", "title_x"], ascending=[True, False]))