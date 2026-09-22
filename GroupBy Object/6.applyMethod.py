""" Topic 6. apply() -> built-in function """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:/PANDAS/GroupBy Object/imdb-top-1000.csv")

# Group the movies according to Genre.
genres = top_movies.groupby("Genre")


# find number of movies starting with A for each group
def foo(group):
    return group['Series_Title'].str.startswith('A').sum()

# print(genres.apply(foo))

# find ranking of each movie in the group according to IMDB rating
def rank_movie(group):
    group['movie_rank_in_genre'] = group['IMDB_Rating'].rank(ascending=False)
    return group

print(genres.apply(rank_movie))

# find normalized IMDB Rating group wise
def normalization(group):
    group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min()) / (group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
    return group

print(genres.apply(normalization))