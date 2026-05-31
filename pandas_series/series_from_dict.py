""" Topic:1. Creating Series from Dictonary """

import numpy as np
import pandas as pd


#series from dict
marks = {
    "English": 84,
    "Maths": 86,
    "Physics": 84,
    "Chemistry": 83,
    "Painting": 97
}
marks_series = pd.Series(marks, name="Chiku ke Marks")
print(marks_series)