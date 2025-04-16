# This R program shows how to create a simple line graph of monthly temperatures

# Load required library
library(ggplot2)

# Sample data: months and average temperatures
months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun")
temps <- c(30, 32, 35, 40, 42, 45)
data <- data.frame(Month = months, Temperature = temps)

# Create the line plot
ggplot(data, aes(x = Month, y = Temperature, group = 1)) +
  geom_line(color = "blue", size = 1.2) +         # Draws the line
  geom_point(color = "red", size = 3) +           # Adds points on the line
  labs(
    title = "Monthly Temperature Trends",
    x = "Month",
    y = "Temperature (°C)"
  ) +
  theme_minimal()  # Applies a clean theme
