from abc import ABC, abstractmethod

class shape(ABC):
    def display(self):
        print("Normal Method")
    @abstractmethod
    def area(self):
        print("abstract method")

# a=shape()    It will give error
# a.area()

class rectangle(shape):
    def area(self):
        print("area method implemented")

r=rectangle()
r.area()
r.display()
