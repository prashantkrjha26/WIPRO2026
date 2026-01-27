# Question – Class Types & Inheritance

# Topics: Class types, Introduction to Inheritance, Types of Inheritance

# 1. Create a base class Vehicle with a method start()
# 2. Create a derived class Car that inherits from Vehicle
# 3. Add a class variable to track the number of vehicles created
# 4. Demonstrate single inheritance and multilevel inheritance with appropriate classes


class Vehicle:
    # Class variable to track number of vehicles
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")


# Single Inheritance: Car inherits from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")


# Multilevel Inheritance: ElectricCar inherits from Car
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


# Creating objects
v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Calling methods
v1.start()
c1.start()
c1.drive()

e1.start()
e1.drive()
e1.charge()

# Display total vehicles created
print("Total vehicles created:", Vehicle.vehicle_count)
