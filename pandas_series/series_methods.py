""" Topic:5. Series methods """

import numpy as np
import pandas as pd


#head and tail
subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
print(subscribers.head())

vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
print(vk.tail(7))


#sample
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
print(movies.sample())


#value_counts
flim = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
print(flim.value_counts())


#sort_values -> inplace
virat_kohli = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
print(virat_kohli.sort_values())


#sort_index -> inplace
flims = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
print(flims.sort_index())