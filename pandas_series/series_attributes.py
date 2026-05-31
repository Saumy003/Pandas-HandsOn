""" Topic:3. Series Attributes """

import numpy as np
import pandas as pd


#sample dict
marks = {
    "English": 84,
    "Maths": 86,
    "Physics": 84,
    "Chemistry": 83,
    "Painting": 97
}
marks_series = pd.Series(marks, name="Chiku ke Marks")


#size
marks_series.size                               #5


#dtype
marks_series.dtype                              #int64


#name
marks_series.name                               #Chiku ke Marks


#is_unique
pd.Series([84, 86, 84, 83, 97]).is_unique       #False
pd.Series([1 ,2, 3, 4, 5]).is_unique            #True


#index
marks_series.index                             #Index(['English', 'Maths', 'Physics', 'Chemistry', 'Painting'], dtype='str')


#values
marks_series.values                            #[84 86 84 83 97]