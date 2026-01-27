# Question – Introduction to OOPs, Classes & Objects

# Topics: Introduction to OOPs, Understanding Classes & Objects

# Create a class Student that:

# 1. Has attributes name and roll_no
# 2. Has a method display_details() to print student information
# 3. Create at least two objects of the class and display their details


# Define the Student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("-" * 20)


# Create objects of the Student class
student1 = Student("Prashant", 1)
student2 = Student("Rohit", 2)

# Display student details
student1.display_details()
student2.display_details()
