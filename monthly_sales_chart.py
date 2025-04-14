# This program creates a simple bar chart to visualize monthly sales

import matplotlib.pyplot as plt  # Importing the plotting library, which is crucial for the visualization

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',' Aug']
sales = [150, 200, 180, 220, 210, 190,230,132]

# Create the bar chart
plt.bar(months, sales, color='skyblue')  # Bar chart with custom color
plt.title('Monthly Sales Overview')  # Title of the chart
plt.xlabel('Month')  # X-axis label
plt.ylabel('Sales ($)')  # Y-axis label
# Display the chart
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Render the plot
