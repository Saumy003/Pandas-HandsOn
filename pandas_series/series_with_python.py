""" Topic:9. Series with Python Functionalities """

import numpy as np
import pandas as pd

subscribers = pd.read_csv("D:\PANDAS\pandas_series\subs.csv").squeeze()
vk = pd.read_csv("D:\PANDAS\pandas_series\kohli_ipl.csv", index_col="match_no").squeeze()
movies = pd.read_csv("D:\PANDAS\pandas_series\\bollywood.csv", index_col="movie").squeeze()


#len/type/dir/sorted/max/min
print(len(subscribers))
print(type(subscribers))
print(sorted(subscribers))
print(min(subscribers))
print(dir(subscribers))


#type conversion
marks = {
    "English": 84,
    "Maths": 86,
    "Physics": 84,
    "Chemistry": 83,
    "Painting": 97
}
marks_series = pd.Series(marks, name="Chiku ke Marks")
print(list(marks_series))
print(dict(marks_series))


# membership operator
print("Awara Paagal Deewana" in movies)         #will run on index values

print("Aditya Roy Kapoor" in movies.values)


#looping
for i in movies:
    print(i)                 #loop will run on values

for j in movies.index:
    print(j)

#arithmetic operators
print(100 - marks_series)   #broadcasting


#relational operators
print(vk >= 50)