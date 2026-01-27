class calc:
    def add(self,a,b=0.,c=0):
        return a+b+c
c=calc()
print(c.add(10))
print(c.add(20,30))
print(c.add(50,60,80))



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