# This Python program creates a simple line graph of monthly temperatures

import matplotlib.pyplot as plt  # Import plotting library

# Sample data: months and temperatures
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temps = [30, 32, 35, 40, 42, 45]

# Create the line graph
plt.plot(months, temps, marker='o', color='blue', linewidth=2, label='Temperature')

# Add title and labels
plt.title('Monthly Temperature Trends')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
