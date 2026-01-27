# Question – Descriptors

# Topic: Descriptors

# Create a class Employee with attributes:
# name
# salary

# Implement a descriptor that:

# 1. Ensures salary is always a positive number
# 2. Raises a ValueError if a negative salary is assigned
# 3. Demonstrates the descriptor by creating multiple Employee objects

class PositiveSalary:
    def __get__(self, instance, owner):
        return instance.__dict__.get("salary")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance.__dict__["salary"] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Demonstration with multiple Employee objects
emp1 = Employee("Prashant", 50000)
emp2 = Employee("Rohit", 65000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# This will raise ValueError
# emp2.salary = -20000
