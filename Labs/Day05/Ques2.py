# Question – Polymorphism (Method & Operator Overloading)


# Topics: Introduction to Polymorphism, Polymorphism on Operators

# 1. Create a class Calculator that demonstrates method overriding
# 2. Create another class AdvancedCalculator that overrides a
# method from Calculator
# 3. Implement operator overloading by overloading the + operator
# to add two objects of a custom class
# 4. Demonstrate polymorphism using the same method name with different behaviors



# Polymorphism: Method Overriding & Operator Overloading

# 1. Base class demonstrating method overriding
class Calculator:
    def calculate(self, a, b):
        return a + b   # addition


# 2. Derived class overriding the same method
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b   # multiplication


# 3. Custom class for operator overloading
class Number:
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    def show(self):
        print(self.value)


# MAIN PROGRAM

# Method overriding demonstration
calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator result:", calc.calculate(5, 3))        # 8
print("AdvancedCalculator result:", adv_calc.calculate(5, 3))  # 15


# Polymorphism using same method name
calculators = [Calculator(), AdvancedCalculator()]

print("\nPolymorphism Output:")
for obj in calculators:
    print(obj.calculate(4, 2))


# Operator overloading demonstration
n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2   # + operator overloaded
print("\nOperator Overloading Result:")
n3.show()      # 30
