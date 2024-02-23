import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Volume': [1000000, 1500000, 1200000, 1400000, 1100000, 1600000],
    'Price': [2700, 2720, 2750, 2740, 2760, 2770]
}
alphabet_stock_data = pd.DataFrame(data)
alphabet_stock_data['Date'] = pd.to_datetime(alphabet_stock_data['Date'])
alphabet_stock_data.set_index('Date', inplace=True)
start_date = '2023-01-02'
end_date = '2023-01-05'
filtered_data = alphabet_stock_data[start_date:end_date]
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Volume'], filtered_data['Price'], color='blue', marker='o')
plt.title('Scatter Plot of Trading Volume vs. Stock Prices')
plt.xlabel('Trading Volume')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()
