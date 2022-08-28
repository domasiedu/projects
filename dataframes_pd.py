"""
Pandas as a high-level data manipulation tool developed by Wes McKinney.
DataFrames allows one to store and manipulate tabular data in rows of
observations and columns of variables
"""

import pandas as pd

dict1 = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98]}


brics = pd.DataFrame(dict1)
print(brics)

