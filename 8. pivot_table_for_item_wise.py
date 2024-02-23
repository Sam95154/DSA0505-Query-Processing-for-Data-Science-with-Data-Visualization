import pandas as pd
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Unit Sold': [5, 10, 8, 12, 15, 9, 16, 11, 7, 13]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(sales_data, values='Unit Sold', index='Item', aggfunc='sum')
print(pivot_table)
