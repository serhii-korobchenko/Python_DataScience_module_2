import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

print(data)

data = data.dropna()

print(data)