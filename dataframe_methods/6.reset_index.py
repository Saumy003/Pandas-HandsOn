""" Topic 6. Reset_index """

import numpy as np
import pandas as pd

batsman = pd.read_csv("D:\\PANDAS\\dataframe_methods\\batsman_runs_ipl.csv")

marks = {
    "maths" : 97,
    "hindi" : 88,
    "science" : 93,
    "english" : 94
}
marks_series = pd.Series(marks)

# reset_index (DataFrame)
batsman.set_index("batter")
print(batsman.reset_index())

# 
batsman["batting_rank"] = batsman["batsman_run"].rank(ascending=False)
batsman.set_index("batter")
print(batsman.reset_index())

# series to dataframe using reset_index
print(marks_series.reset_index())