# 1. Database Connectivity (MySQL / MongoDB)

# Question:
# You are tasked with managing employee data stored in a database.

# Part A: MySQL

# Connect to a MySQL database company_db (assume username, password, host are given).

# The database has a table employees with columns: id, name, department, salary.

# Write Python code to:
# 1. Fetch all employees whose salary is greater than 50,000.

# 2. Insert a new employee record into the table.

# 3. Update the salary of a specific employee by 10%.

# Part B: MongoDB

# Connect to a MongoDB database company_db and collection employees.

# Insert a new employee document with fields: name, department, salary.

# Find all employees in the "IT" department.

# Update the salary of an employee with a given name.





# Part A
import mysql.connector

try:

    # Connect to MySQL

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prashant@26",
        database="company_db"
    )

    cursor = conn.cursor()
    print("Connected to the Database Successfully")



    # 1. Fetch employees with salary > 50000

    print("\nEmployees with salary > 50000:\n")

    select_query = "SELECT * FROM employees WHERE salary > %s"
    cursor.execute(select_query, (50000,))
    result = cursor.fetchall()

    if result:
        for row in result:
            print(row)
    else:
        print("No employees found with salary > 50000")


    # -----------------------------
    # 2. Insert new employee
    # -----------------------------
    insert_query = """
    INSERT INTO employees (name, department, salary)
    VALUES (%s, %s, %s)
    """

    values = ("Pankaj", "HR", 50000)

    cursor.execute(insert_query, values)
    conn.commit()

    print("\nNew employee inserted successfully!")
    print("Rows inserted:", cursor.rowcount)



    # 3. Update salary by 10%

    update_query = """
    UPDATE employees
    SET salary = salary * 1.10
    WHERE name = %s
    """

    cursor.execute(update_query, ("Supriya",))
    conn.commit()

    if cursor.rowcount > 0:
        print("Salary updated by 10% successfully!")
    else:
        print("Employee not found for update.")


except mysql.connector.Error as err:
    print("Database Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\nConnection closed.")





# Part B - MongoDB


from pymongo import MongoClient


try:
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    db = client["company_db"]
    collection = db["employees"]


    # Insert new employee document

    employee_doc = {
            "name": "Prashant Kumar Jha",
            "department": "IT",
            "salary": 60000
        }

    collection.insert_one(employee_doc)
    print("\nMongoDB: Employee inserted successfully!")


    # Find all employees in IT department

    print("\nMongoDB: Employees in IT department:\n")

    it_employees = collection.find({"department": "IT"})

    for emp in it_employees:
        print(emp)


    # Update salary of employee by name

    collection.update_one(
            {"name": "Prashant Kumar Jha"},
            {"$set": {"salary": 80000}}
        )

    print("\nMongoDB: Salary updated successfully!")

except Exception as e:
        print("MongoDB Error:", e)



