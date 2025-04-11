# This program shows how horsepower affects fuel efficiency using a scatterplot
# It uses the mpg dataset and plots horsepower against mpg
# This helps you learn how to visualize data using ggplot2 in R

install.packages("tidyverse") #If you don't have tidyverse, you could install it to use ggplot2

# Load the required library
library(ggplot2)  # This library is used to create customizable plots

# Load the mpg dataset that comes with ggplot2
data(mpg)  # This is the dataset used in this visualization

# Create a scatterplot with a regression line
ggplot(data = mpg, aes(x = hwy, y = displ)) +  # Sets x as highway mpg, y as engine displacement
  geom_point(color = "blue", size = 3) +  # Adds blue points to the graph
  geom_smooth(method = "lm", se = FALSE, color = "red") +  # Adds a red regression line
  labs(
    title = "Engine Displacement vs Highway MPG",  # Sets the title of the plot
    x = "Highway Miles Per Gallon",  # X-axis label
    y = "Engine Displacement (litres)"  # Y-axis label
  ) +
  theme_minimal()  # Applies a clean, simple theme to the plot
