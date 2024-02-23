import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, np.nan, 5]
}
df = pd.DataFrame(data)
missing_values = df.isnull()
print(missing_values)
