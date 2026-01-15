numbers=[10,20,30,40]
names=["Ram","Hari","Ramhya"]
mixed=[1, "Python",3.5,"True"]
print(numbers)
print(names)
print(mixed)
print(numbers[0:3])

numbers[1]=100
print(numbers)

for i in numbers:
    print(i)

if 10 in numbers:
    print("Found")

matrix=[[1,2,3],[4,5,6]]
print(matrix)
print(matrix[1][2])

names.reverse()
print(names)

names.append("kajal")
print(names)

names.extend(["pavan","leela"])
print(names)

names.remove("kajal")
print(names)

names.insert(3,"Uma")
print(names)