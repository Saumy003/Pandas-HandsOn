""" Topic:11. Plotting Graphs on Series """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()


#plotting graphs

#ex1.
subscribers.plot()
plt.show()

#ex 2.
x = pd.Series([100, 50, 300, 290, 150, 400])

x.plot()
plt.show()


#ex 3.
print(movies.value_counts().head(20))       #--> top 20 actors who has made more than 20 movies

movies.value_counts().head(20).plot(kind="bar")
plt.show()

movies.value_counts().head(20).plot(kind="pie")
plt.show()