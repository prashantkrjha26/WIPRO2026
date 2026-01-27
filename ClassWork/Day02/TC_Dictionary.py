student={
    "name":"Prashant",
    "age":20,
    "course":"Python"
}
print(student)
print(student["name"])
print(student.get("age"))

student["Marks"]=85
student["age"]=25
print(student)
print(student["name"])
print(student.get("age"))
print(student)
student.pop("age")
print(student)
student.popitem()
print(student)


print(student.keys())
print(student.values())

for key in student:
    print(key,student[key])

if "name" in student:
    print("key exist")


employees={

    101:{"name":"Prashant","salary":2000},
    102:{"name":"leena","salary":2000}
}

print(employees[101]["name"])