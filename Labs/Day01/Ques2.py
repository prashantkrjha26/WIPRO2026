# Question – List, Dictionary & Set Comprehensions

# Topic: Comprehensions in Python

# data = [1,2,3,4,5,6,2,4]
# Write a program to:

# 1. Create a list comprehension to store squares of all numbers
data = [1,2,3,4,5,6,2,4]
squared_list = [x**2 for x in data]
print(squared_list)


# 2. Create a set comprehension to store only unique even numbers
data = [1,2,3,4,5,6,2,4]
even_set = {x for x in data if x % 2 == 0}
print(even_set)


# 3. Create a dictionary comprehension where the key is
# the number and the value is its cube
data = [1,2,3,4,5,6,2,4]
cube_dict = {x: x**3 for x in data}
print(cube_dict)