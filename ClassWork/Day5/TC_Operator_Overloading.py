class box1:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value


b1=box1(50)
b2=box1(30)
b3=box1(20)
print(b1+b2)

# print(b1+b2+b3)   it will give error

print(b1+b3)

# Another way
class Calc:
    def add(self, *params):
        total = 0
        for x in params:
            total += x
        return total


c = Calc()
print(c.add(2, 3))
print(c.add(2, 3, 4))
print(c.add(1, 2, 3, 4, 5))