# 2. Data Analysis / Processing (NumPy / Pandas)

# Question:
# You have sales data for a store in a CSV file sales.csv:
# Date	     Product	Quantity	      Price
# 1/1/2025	  A	         10	               50
# 1/2/2025	  B	         5	               30
# 1/3/2025	  C	         12	               40
# 1/4/2025	  A	         7	               50


# Write Python code to:

# 1. Load the CSV into a Pandas DataFrame.

# 2. Add a new column "Total" which is Quantity * Price.

# 3. Using NumPy, calculate the total sales, average daily sales,
# and standard deviation of daily sales.

# 4. Find the best-selling product based on total quantity sold.





# 1. Load the CSV into a Pandas DataFrame.

import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")
print("\nGiven DataFrame:\n")
print(df)

# 2. Add a new column "Total" which is Quantity * Price.

df["Total"] = df["Quantity"] * df["Price"]

print("\nUpdated DataFrame:\n")
print(df)


# 3. Using NumPy, calculate:
#    - Total sales
#    - Average daily sales
#    - Standard deviation of daily sales

daily_sales = df.groupby("Date")["Total"].sum()

total_sales = np.sum(daily_sales.values)
average_daily_sales = np.mean(daily_sales.values)
std_daily_sales = np.std(daily_sales.values)

print("\nSales Statistics:\n")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_daily_sales)


# 4. Find the best-selling product based on total quantity sold.

product_quantity = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_quantity.idxmax()

print("\nBest Selling Product:", best_selling_product)


# Add CSV file in the code folder and name should be "sales.csv" & add this data in that:
# Date,Product,Quantity,Price
# 1/1/2025,A,10,50
# 1/2/2025,B,5,30
# 1/3/2025,C,12,40
# 1/4/2025,A,7,50

