import matplotlib.pyplot as plt  # Importing the plotting library
import numpy as np  # For generating sample data

#Sample data: Height (in cm) and Weight (in kg)
height = np.array([160, 170, 180, 190, 200, 210, 220, 230])
weight = np.array([55, 60, 65, 70, 75, 80, 85, 90])

# Create the scatter plot
plt.scatter(height, weight, color='blue', marker='o')  # Scatter plot with blue dots
plt.plot(height, weight, color='blue')     # Displays a line through the scatter plot (optional)
# Add title and labels
plt.title('Height vs Weight')  # Title of the plot
plt.xlabel('Height (cm)')  # Label for the X-axis
plt.ylabel('Weight (kg)')  # Label for the Y-axis

# Display the plot
plt.show()  # Render the plot
