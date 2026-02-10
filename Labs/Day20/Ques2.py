# 2. DataFrames

# Question:
# You have the following DataFrame:
# Employee                  Department               Salary
# John                        IT                      50000
# Alice                       HR                      60000
# Bob                         IT                      55000
# Eva                         Finance                 65000
# Mark                        HR                      62000

# Write code to:

# 1. Filter all employees from the "IT" department.

# 2. Find the average salary per department.

# 3. Add a new column "Salary_Adjusted" which increases each employee's salary by 10%.



import pandas as pd

# Create the DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# 1. Filter employees from IT department
it_employees = df[df["Department"] == "IT"]

# 2. Average salary per department
avg_salary_per_dept = df.groupby("Department")["Salary"].mean()

# 3. Add Salary_Adjusted column (10% increase)
df["Salary_Adjusted"] = df["Salary"] * 1.10

# Print results
print("IT Department Employees:")
print(it_employees)

print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

print("\nUpdated DataFrame:")
print(df)
