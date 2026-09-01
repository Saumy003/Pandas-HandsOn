""" Topic 5. Set index """

import numpy as np
import pandas as pd

# set_index (DataFrame)
batsman = pd.read_csv("D:\\PANDAS\\dataframe_methods\\batsman_runs_ipl.csv")
print(batsman)

print(batsman.set_index("batter"))