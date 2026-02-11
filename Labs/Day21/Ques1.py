# 3. Matplotlib / Seaborn (Data Visualization)

# Question:
# Given the following dataset of monthly sales:

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# sales = [25000, 27000, 30000, 28000, 32000, 31000]

# Plot a line chart of monthly sales using Matplotlib.

# Using Seaborn, create a bar plot for the same dataset.

# Customize the plots with title, x - axis label, y-axis label, and grid lines.




import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Monthly sales dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]


# Line Chart using Matplotlib


plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker='o', linestyle='-', linewidth=2)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.grid(True)
plt.tight_layout()
plt.show()



# Bar Plot using Seaborn


# Set seaborn style
sns.set_style("whitegrid")

# Convert dataset into DataFrame
data = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

plt.figure(figsize=(8, 5))

sns.barplot(x="Month", y="Sales", data=data)

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.grid(True)
plt.tight_layout()
plt.show()
