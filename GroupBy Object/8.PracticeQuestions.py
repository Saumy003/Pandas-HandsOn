""" Topic 8. Practice Questions on GroupBy Objects """

import numpy as np
import pandas as pd

# Data set of IPL Deliveries (ball by ball).
ipl_deliveries = pd.read_csv(r"D:/PANDAS/GroupBy Object\deliveries.csv")

# find the top 10 batsman in terms of runs
print(ipl_deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

# find the batman with max number of sixes
six = ipl_deliveries[ipl_deliveries['batsman_runs'] == 6]
print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])

# find batsman with most number of 4's and 6's in last 5 overs
overs = ipl_deliveries[ipl_deliveries['over'] > 15]
sixes_and_fours = overs[(overs['batsman_runs'] == 4) | (overs['batsman_runs'] == 6)]
print(sixes_and_fours.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1))

# find V.Kohli runs against all teams
temp_df = ipl_deliveries[ipl_deliveries['batsman'] == 'V Kohli']
print(temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index())

# Create a function that can return the highest score of any batsman

def highest(batsman):
    df = ipl_deliveries[ipl_deliveries['batsman'] == batsman]
    return df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(highest('CH Gayle'))