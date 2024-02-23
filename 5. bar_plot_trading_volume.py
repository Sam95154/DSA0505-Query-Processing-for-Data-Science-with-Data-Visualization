import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Volume': [1000000, 1500000, 1200000, 1400000, 1100000, 1600000]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
start_date = '2023-01-02'
end_date = '2023-01-05'
filtered_df = df[start_date:end_date]
plt.figure(figsize=(10, 6))
plt.bar(filtered_df.index, filtered_df['Volume'], color='blue')
plt.title('Alphabet Inc. Stock Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()
