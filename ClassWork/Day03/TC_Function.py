def add(a,b):
    print(a+b)

def subtract(a,b):
    return a-b,a

add(10,20)
print(subtract(100,20))

def hello(greeting="Hello", name="world"):
    print('%s,%s!'%(greeting,name))
hello()
hello('Greeting','Prashant')


def print_param(*params):
    print(params)
print_param('Testing')
print_param(1,2,3,4)

def print_param_1(**params):
    print(params)

print_param_1(x=1,y=2,z=3)