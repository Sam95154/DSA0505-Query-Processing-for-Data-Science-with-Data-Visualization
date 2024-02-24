import matplotlib.pyplot as plt
import numpy as np
h1 = np.random.normal(160, 10, 50)  # Mean height: 160 cm, Standard deviation: 10 cm
w1 = np.random.normal(65, 5, 50)
h2 = np.random.normal(170, 8, 50)
w2 = np.random.normal(75, 6, 50)
h3 = np.random.normal(155, 12, 50)
w3 = np.random.normal(60, 7, 50)
plt.scatter(h1, w1, label='Group 1', color='blue', marker='o')
plt.scatter(h2, w2, label='Group 2', color='red', marker='*')
plt.scatter(h3, w3, label='Group 3', color='green', marker='s')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot: Heights vs. Weights for Three Groups')
plt.legend()
plt.grid(True)
plt.show()
