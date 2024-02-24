import matplotlib.pyplot as plt

# Sample data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))  # Set the figure size

plt.barh(languages, popularity, color='skyblue')

# Add labels and a title
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# Display the values at the end of the bars
for i, value in enumerate(popularity):
    plt.text(value, i, str(value), va='center')

# Show the plot
plt.tight_layout()
plt.show()
