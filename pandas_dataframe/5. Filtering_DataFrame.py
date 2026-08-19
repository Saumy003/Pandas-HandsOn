""" Topic: 5 Filtering a DataFrame """

import numpy as np
import pandas as pd

matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")
movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")

# select first 2 rows from matches
print(matches.head(2))

# find all final winners
mask = matches["MatchNumber"] == "Final"
new_df = matches[mask]
print(new_df[["Season", "WinningTeam"]])

# how many super over match hs occured
sp = matches["SuperOver"] == "Y"
matches[sp]
print(matches[sp].shape[0])

# how many matches has csk won in kolkata
place = matches["City"] == "Kolkata"

team = matches["WinningTeam"] == "Chennai Super Kings"

print(matches[(place) & (team)])


# toss winner is match winner in percentage
winner = matches["TossWinner"] == matches["WinningTeam"]
print(matches[winner].shape[0] / matches.shape[0])
"""percentage is :"""
print((matches[winner].shape[0] / matches.shape[0]) * 100)

# movies with rating higher than 8 and votes more than 10000

(movies["imdb_rating"] > 8) & (movies["imdb_votes"] > 10000)
print(movies[(movies["imdb_rating"] > 8) & (movies["imdb_votes"] > 10000)].shape[0])

# action movies with rating higher than 7.5
movies["genres"].str.split("|")
mask1 = movies["genres"].str.contains("Action")
mask2 = movies["imdb_rating"] > 7.5

print(movies[(mask1) & (mask2)])
