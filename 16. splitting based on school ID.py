import pandas as pd
data = {'StudentID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'SchoolCode': ['S001', 'S002', 'S001', 'S002', 'S001']}
df = pd.DataFrame(data)
grouped = df.groupby('SchoolCode')
for name, group in grouped:
    print(f"Group: {name}")
    print(group)
    print("\n")
print(f"Type of GroupBy object: {type(grouped)}")
