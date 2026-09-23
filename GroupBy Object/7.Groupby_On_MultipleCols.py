""" Topic 6. groupby on multiple cols """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:/PANDAS/GroupBy Object/imdb-top-1000.csv")

# Grouping between Multiple Columns (Director ans Star1).
duo = top_movies.groupby(["Director", "Star1"])


# size -> to possible group made of the combination
print(duo.size())

# get_group() -> to get a paticular combination of group
print(duo.get_group(('Aamir Khan', 'Amole Gupte')))

# find the most earning actor <-> director combo
print(duo['Gross'].sum(numeric_only=True).sort_values(ascending=False).head(1))

# find the best(in-terms of avg metascore) actor <-> genre combo
best_genre_for_actor = top_movies.groupby(['Star1', 'Genre'])
print(best_genre_for_actor['Metascore'].mean().reset_index().sort_values('Metascore', ascending=False).head(1))

# agg on multiple groupby
print(duo.agg(['min', 'max']))