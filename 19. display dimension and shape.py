import pandas as pd
data = {
    'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany'],
    'Beer': [25, 20, 15, 22, 18],
    'Spirit': [10, 8, 7, 12, 9],
    'Wine': [5, 7, 8, 4, 7],
}
df = pd.DataFrame(data)
dimensions = df.shape
print(f"Dimensions of the dataset: {dimensions}")
column_names = df.columns
print("Column names:")
for column in column_names:
    print(column)
