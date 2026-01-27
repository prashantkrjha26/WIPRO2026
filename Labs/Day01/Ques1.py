# Question – Widely Used Built-in Functions & Lambda

# Topic: range, enumerate, iter, map, filter, reduce, lambda

# 1. Uses range() to generate numbers from 1 to 20

for i in range(1,21):
    print(i)


# 2. Uses filter() with a lambda to select only even numbers
numbers = range(1,21)
evennumbers=list(filter(lambda x:x%2==0,numbers))
print(evennumbers)


# 3.  Uses map() with a lambda to square the filtered numbers
numbers = range(1,21)

sqnum=list(map(lambda x:x**x,numbers))
print(sqnum)


# 4. Uses reduce() to calculate the sum of squared even numbers
from functools import reduce
numbers=[1,2,3,4,5,6]

result = reduce(lambda acc, x: acc + x**2 if x% 2 ==0 else acc, numbers, 0)
print(result)


# 5. Uses enumerate() to print the index and value of the final result list
numbers = [1,2,3,4,5,6]

final_result=[x**2 for x in numbers if x % 2 ==0]


for index, value in enumerate(final_result):
    print(index,value)