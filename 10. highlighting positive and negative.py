import pandas as pd
import numpy as np

# Create a DataFrame with ten rows and four columns with random values
np.random.seed(42)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Define a formatting function to apply color based on the value
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply the formatting function to the DataFrame
formatted_df = df.applymap(color_negative_red)

# Display the formatted DataFrame
print(formatted_df)
