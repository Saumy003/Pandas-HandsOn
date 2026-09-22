""" Topic 5. Aggregate Methods -> used to apply one or more operations over a grouped axis after calling """

import numpy as np
import pandas as pd

# Data set of Movies.
top_movies = pd.read_csv(r"D:/PANDAS/GroupBy Object/imdb-top-1000.csv")

# Group the movies according to Genre.
genres = top_movies.groupby("Genre")

# agg method -> passing dict
print(genres.agg(
    {
        'Runtime' : 'mean',
        'IMDB_Rating' : 'mean',
        'No_of_Votes' : 'sum',
        'Gross' : 'sum',
        'Metascore' : 'min'
    }
))

# agg method -> passing list
print(genres.agg(['min', 'max']))

# looping in group

df = pd.DataFrame({
    'Department': ['Sales', 'HR', 'Sales', 'HR', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Salary': [50000, 60000, 55000, 65000, 70000]
})

for dept_name, dept_df in df.groupby('Department'):           # Iterate through each group
    print(f"Department: {dept_name}")
    print(dept_df)
    print("-" * 20)