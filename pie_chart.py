# This program creates a pie chart to show the percentage distribution of expenses

import matplotlib.pyplot as plt  # Library used for plotting

# Sample data: Categories and corresponding expenses
categories = ['Rent', 'Food', 'Transport', 'Utilities', 'Savings']
expenses = [1200, 600, 300, 200, 700]

# Create the pie chart
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expense Distribution')  # Add a title
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()  # Display the chart
