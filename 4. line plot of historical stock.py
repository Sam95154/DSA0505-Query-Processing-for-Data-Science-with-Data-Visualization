import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Price': [2700, 2720, 2750, 2740, 2760, 2770]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
start_date = '2023-01-02'
end_date = '2023-01-05'
filtered_df = df[start_date:end_date]
plt.figure(figsize=(10, 6))
plt.plot(filtered_df.index, filtered_df['Price'], marker='o', linestyle='-')
plt.title('Alphabet Inc. Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()
