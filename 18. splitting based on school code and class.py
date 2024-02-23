import pandas as pd
data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'School Code': [101, 102, 101, 103, 102],
        'Class': ['A', 'B', 'A', 'C', 'B'],
        'Age': [15, 17, 14, 16, 18]}
df = pd.DataFrame(data)
grouped = df.groupby(['School Code', 'Class'])
for (school_code, class_), group in grouped:
    print(f"School Code: {school_code}, Class: {class_}")
    print(group)
    print()
