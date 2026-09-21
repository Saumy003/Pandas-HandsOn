""" Topic 4. GroupBy Attributes & Methods """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:/PANDAS/GroupBy Object/imdb-top-1000.csv")

# Group the movies according to Genre.
genres = top_movies.groupby("Genre")


# find total number of groups -> len
print(len(genres))

# find items in each group -> size
print(genres.size())

# find first member of each group -> first()
print(genres.first())

# find last member of each group -> last()
print(genres.last())

# find nth member of each group -> nth()
print(genres.nth(6))

# find single specific group as a subset from GroupBy object -> get_group()
print(genres.get_group('Horror'))

# to generate summary statistics for each group in your dataset -> describe()
print(genres.describe())

# to extract a random sample of rows from each individual group -> sample()
print(genres.sample())

# to count the number of distinct (unique) elements within each group -> nunique()
print(genres.nunique())