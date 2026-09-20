""" Topic 10. drop_duplicates() ->(series + dataframes) """

import numpy as np
import pandas as pd

temp = pd.Series([1, 1, 1, 1, 3, 4, 2, 1, 2, 3, np.nan, np.nan, 2, 3 ])
print(temp.drop_duplicates())         # --> remove duplicate row.

print(temp.drop_duplicates(keep="first"))  # keep parameter -> keeps first occurance or last occurance.


# Ques 1. Find the last matchplayed by virat kohli in Delhi
matches = pd.read_csv("D:\PANDAS\pandas_dataframe\ipl-matches.csv")

matches["all_players"] = matches["Team1Players"] + matches["Team2Players"]

def did_kohli_play(players_list):
    return "V Kohli" in players_list

matches["kolhi played"] = matches["all_players"].apply(did_kohli_play)
recent_kolhi_match_in_Delhi = matches[(matches["City"] == "Delhi") & (matches["kolhi played"] == True)].drop_duplicates(subset=['City', 'kolhi played'], keep="first")

print(recent_kolhi_match_in_Delhi)