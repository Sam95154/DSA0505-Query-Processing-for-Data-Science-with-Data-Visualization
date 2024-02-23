import pandas as pd
data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'School Code': [101, 102, 101, 103, 102],
        'Age': [15, 17, 14, 16, 18]}
df = pd.DataFrame(data)
grouped = df.groupby('School Code')['Age'].agg(['mean', 'min', 'max'])
grouped.reset_index(inplace=True)
print(grouped)
