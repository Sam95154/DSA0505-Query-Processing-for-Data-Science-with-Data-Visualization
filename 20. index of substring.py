import pandas as pd
data = {
    'Text': ['Hello, world', 'This is a test', 'Pandas is great', 'DataFrames are useful']
}
df = pd.DataFrame(data)
substring = 'is'
result = df['Text'].str.find(substring)
print("Index of substring 'is' in the 'Text' column:")
print(result)
