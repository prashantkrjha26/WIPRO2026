# Question – Iterators and Generators

# Topic: Iterators & Generators

# 1. Create a custom iterator class that iterates over numbers from 1 to N

class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


n = 5
for num in NumberIterator(n):
    print(num)


# 2. Create a generator function that yields the first N Fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print("Fibionacci:")
for num in fibonacci(5):
    print(num)
n = 7
for num in fibonacci(n):
    print(num)


# 3. Demonstrate the difference between using the iterator
# and generator by printing values using a for loop


# Through Iterator
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


print("Using Iterator:")
for num in NumberIterator(5):
    print(num)


# Through Generator
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Using Generator:")
for num in fibonacci(5):
    print(num)
