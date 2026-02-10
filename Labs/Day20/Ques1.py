# 1. NumPy / Pandas (Data Manipulation)

# Question:
# You have a dataset of student scores in a class as a Python list of dictionaries:

# students = [
#         {"name": "Alice", "score": 85},
#         {"name": "Bob", "score": 92},
#         {"name": "Charlie", "score": 78},
#         {"name": "David", "score": 90},
#         {"name": "Eva", "score": 88}
#           ]

# Convert this data into a Pandas DataFrame.

# Using NumPy, calculate the mean, median,and standard deviation of the students' scores.

# Add a new column to the DataFrame called "above_average" which is True
# if the student's score is above the mean and False otherwise.




import pandas as pd
import numpy as np

# Given data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

# Convert to DataFrame
df = pd.DataFrame(students)

# Calculate statistics using NumPy
mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_deviation = np.std(df["score"])

# Add above_average column
df["above_average"] = df["score"] > mean_score

# Print results
print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_deviation)
print("\nDataFrame:")
print(df)
