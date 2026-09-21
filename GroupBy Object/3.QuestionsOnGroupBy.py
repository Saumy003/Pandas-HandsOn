""" Topic 3. Basic Questions on Group By """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:/PANDAS/GroupBy Object/imdb-top-1000.csv")


# Ques 1. find the top 3 genres by total earning
genres = top_movies.groupby('Genre')
print(genres["Gross"].sum(numeric_only=True).sort_values(ascending=False).head(3))

# Ques 2. find the genre with highest avg IMDB rating
print(genres["IMDB_Rating"].mean(numeric_only=True).sort_values(ascending=False).head(1))

# Ques 3. find director with most popularity top 3
directors = top_movies.groupby('Director')
print(directors["No_of_Votes"].sum(numeric_only=True).sort_values(ascending=False).head(3))

# Ques 4. find number of movies done by each actor
actors = top_movies.groupby('Star1')
print(actors['Series_Title'].count().sort_values(ascending=False))