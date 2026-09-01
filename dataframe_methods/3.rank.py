""" Topic 3. Rank method """

import numpy as np
import pandas as pd

# rank(series)
batsman = pd.read_csv("D:\\PANDAS\\dataframe_methods\\batsman_runs_ipl.csv")
print(batsman.sample(4))

batsman["batting_rank"] = batsman["batsman_run"].rank(ascending=False)
print(batsman.head())
print(batsman.sort_values("batting_rank"))