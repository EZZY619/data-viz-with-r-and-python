# This program creates a simple histogram to show the distribution of ages

import matplotlib.pyplot as plt  # Import the plotting library

# Sample data: ages of a group of people
ages = [22, 25, 29, 30, 30, 31, 33, 35, 35, 36, 38, 40, 40, 42, 45, 48, 50, 52, 55, 60]

# Create the histogram
plt.hist(ages, bins=8, color='lightgreen', edgecolor='black')  # 8 bins for grouping the age ranges

# Add labels and title
plt.title('Age Distribution')  # Title of the chart
plt.xlabel('Age')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis

# Display the chart
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()  # Render the plot
