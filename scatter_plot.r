# This program creates a scatter plot to visualize height vs weight

# Sample data: Height (in cm) and Weight (in kg)
height <- c(160, 170, 180, 190, 200, 210, 220, 230)
weight <- c(55, 60, 65, 70, 75, 80, 85, 90)

# Create the scatter plot
plot(height, weight,main = "Height vs Weight",xlab = "Height (cm)", ylab = "Weight (kg)", pch = 19, col = "blue")
