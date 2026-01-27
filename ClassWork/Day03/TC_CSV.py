import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Prashant",1,20])
    writer.writerow(["Rohit",2,21])
    writer.writerow(["Rahul",3,22])