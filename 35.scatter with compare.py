import matplotlib.pyplot as plt
m1 = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
s = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(range,m1, label='Math', color='blue')
plt.scatter(range,s, label='SScience', color='red')
plt.xlabel('Math Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot: Math vs. Science Marks')
plt.legend()
plt.grid(True)
plt.show()
