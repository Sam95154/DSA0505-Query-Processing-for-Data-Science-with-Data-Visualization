import pandas as pd
data = {
    'Text': ['Hello, World', 'This is a Test', 'Pandas is Great', 'DataFrames are Useful']
}
df = pd.DataFrame(data)
column_to_swap = 'Text'
df[column_to_swap] = df[column_to_swap].str.swapcase()
print("DataFrame with Cases Swapped:")
print(df)
