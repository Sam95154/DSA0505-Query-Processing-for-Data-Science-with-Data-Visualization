import pandas as pd
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Sale': [100, 200, 150, 300, 250, 180, 320, 220, 170, 310]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(sales_data, values='Sale', index='Item', aggfunc=[max, min])
pivot_table.columns = ['Max Sale', 'Min Sale']
print(pivot_table)
