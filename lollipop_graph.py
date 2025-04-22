# This program creates a lollipop chart to visualize category values

import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 35, 27]

# Create the lollipop chart
plt.stem(categories, values, basefmt=" ", linefmt="skyblue", markerfmt="o")
plt.title('Lollipop Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')

# Display the plot
plt.tight_layout()
plt.show()
