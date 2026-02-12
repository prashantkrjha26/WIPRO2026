import mysql.connector
host="localhost"
user="root"
password="Prashant@26"
database="wipro2026"


conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("Connected to the Database Successfully")

query="SELECT * FROM wipro2026.employee;"
cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)
