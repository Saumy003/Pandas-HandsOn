""" Topic:10. Boolean Indexing on Series """

import numpy as np
import pandas as pd

subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()


# Find out 50's and 100's scored by kohli.
print(vk >= 50)
print(vk[vk >= 50])
print(vk[vk >= 50].size)          #return no. of matches


# Finds number of ducks
print(vk[vk == 0].size)           #return no. of matches


#Counts number of days person get more than 200 subs a day
print(subscribers[subscribers > 200].size)


# find the actors who have done more than 20 movies
number_of_movies = movies.value_counts()
number_of_movies > 20                            #return in boolean

print(number_of_movies[number_of_movies > 20])