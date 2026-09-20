""" Topic 11. apply() ->(series + dataframes) """

""" apply() is a highly versatile method used to pass a function along an axis
 of a DataFrame (either rows or columns) or to each element of a Series. """


import numpy as np
import pandas as pd

# apply() used in Series #

temp = pd.Series([19, 23, 5, 42, 70])

def sigmoid(value):
    return 1/1 + np.exp(-value)

print(temp.apply(sigmoid))


# apply used in Dataframe #

df = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Price': [1000, 500, 300],
    'Tax_Rate': [0.10, 0.05, 0.08]
})

# Calculate a total price that reads both 'Price' and 'Tax_Rate'
def calculate_total(row):
    return row['Price'] + (row['Price'] * row['Tax_Rate'])

df['Total_Cost'] = df.apply(calculate_total, axis=1)
print(df)
