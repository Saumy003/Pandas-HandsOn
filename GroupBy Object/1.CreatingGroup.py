""" Topic 1. Creating Group of Different Catogary using GroupBy. """

import numpy as np
import pandas as pd

top_movies = pd.read_csv("D:\PANDAS\GroupBy Object\imdb-top-1000.csv")
print(top_movies)

# creating groups --> using GroupBy
genres = top_movies.groupby("Genre")
print(genres)