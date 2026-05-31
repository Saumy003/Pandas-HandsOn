""" Topic:1. Creating Series from lists """

import numpy as np
import pandas as pd

#string
country = ["USA", "India", "Nepal", "Srilanka", "Russia"]
pd.Series(country)


#integer
batsman_runs = [31, 54, 97, 96, 55]
pd.Series(batsman_runs)


#custom index
marks = [93, 88, 89, 94, 94]
subjects = ["English", "Hindi", "Science", "Maths", "SSc."]
pd.Series(marks, index=subjects)


#giving a name to the series
international_runs = [9230, 14797, 4188]
formate = ["TEST", "ODI", "T20i"]
pd.Series(international_runs, index=formate, name="Virat Kohli ke Runs")