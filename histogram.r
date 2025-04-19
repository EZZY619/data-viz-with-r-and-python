# This program creates a simple histogram to show the distribution of ages

# Sample data: ages of a group of people
ages <- c(22, 25, 29, 30, 30, 31, 33, 35, 35, 36, 38, 40, 40, 42, 45, 48, 50, 52, 55, 60)

# Create the histogram
hist(ages,
     breaks = 8,  # Number of bins/groups
     col = "lightgreen",  # Fill color for bars
     border = "black",  # Color of bar borders
     main = "Age Distribution",  # Title of the histogram
     xlab = "Age",  # X-axis label
     ylab = "Frequency"  # Y-axis label
)
