""" Topic 7. Rename(dataframe) """

import numpy as np
import pandas as pd

movies = pd.read_csv("D:\PANDAS\pandas_dataframe\movies.csv")


# rename operation --> use to change column name
print(movies.rename(columns={'imdb_id' : 'imdb' , 'title_x' : 'movie_name'}))


#rename operation --> use to change index
movies.set_index('title_x', inplace=True)
print(movies.rename(index={'Uri: The Surgical Strike' : 'Uri' , 'Battalion 609' : 'Battalion'}))