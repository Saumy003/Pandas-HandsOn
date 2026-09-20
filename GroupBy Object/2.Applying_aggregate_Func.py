""" Topic 2. Applying builtin aggregation functions(sum, mean, median, etc..) on groupby objects. """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:\PANDAS\GroupBy Object\imdb-top-1000.csv")

# Group the movies according to Genre.
genres = top_movies.groupby("Genre")

# Calculate the sum, min, avg of IMDB_Rating of each group.
print(genres.sum(numeric_only=True))
print(genres.min(numeric_only=True))

# recommend version.
print(genres["IMDB_Rating"].mean())



