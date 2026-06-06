""" Topic:6. Series maths methods """
import numpy as np
import pandas as pd


#count
vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
print("Count total number of matches played by virat kohli:",vk.count())


# sum <-> product
subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
print(subscribers.sum())
print(subscribers.product())


#mean -> median -> mode -> std -> var
subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
print(subscribers.mean())

vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
print("Virat Kohli scores median is:",vk.median())

movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()
print("Actor has made maximum number of movies",movies.mode())


#max/min
subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
print("Maximum subs gained in a single day",subscribers.max())
print("Manimum subs gained in a single day",subscribers.min())


#describe
vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
print(vk.describe())

subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
print(subscribers.describe())