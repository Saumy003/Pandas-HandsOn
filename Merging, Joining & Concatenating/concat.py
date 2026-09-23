""" Topic 1. Concat function """

import numpy as np
import pandas as pd

courses = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\courses.csv")
students = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\students.csv")
nov = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\reg-month1.csv")
dec = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\reg-month2.csv")
matches = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\matches.csv")
deliveries = pd.read_csv(r"D:\PANDAS\Merging, Joining & Concatenating\deliveries.csv")

# concat -> vertically mearge two or more dataframes
print(pd.concat([nov, dec]))

# ignore_index
print(pd.concat([nov, dec],ignore_index=True))

# concat as multi-index dataframe
print(pd.concat([nov, dec],keys=['Nov', 'Dec']))

# Multi-index Dataframe -> fetch using iloc
multi = pd.concat([nov, dec], keys=["Nov", "Dec"])
print(multi.loc[("Nov", 0)])
print(multi.loc[("Dec", 4)])

# concat dataframes horizontally
print(pd.concat([nov, dec], axis= 1))
