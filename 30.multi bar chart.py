import matplotlib.pyplot as plt
import numpy as np

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]

# Define the x positions for the bars
x = np.arange(len(men))

bar_width = 0.35

plt.bar(x - bar_width/2, men, bar_width, label='Men', color='blue')
plt.bar(x + bar_width/2, women, bar_width, label='Women', color='red')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.legend()
plt.show()
