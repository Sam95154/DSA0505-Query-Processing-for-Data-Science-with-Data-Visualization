import matplotlib.pyplot as plt
with open('text.txt', 'r') as file:
    data = file.read().split()
x_values = [float(data[i]) for i in range(0, len(data), 2)]
y_values = [float(data[i+1]) for i in range(0, len(data), 2)]

plt.plot(x_values, y_values, marker='o')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot from test.txt')
plt.show()
