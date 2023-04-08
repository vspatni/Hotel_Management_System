# pip install mysql-connector-python

import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@70Fee2fd"
)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXIST pythonTrial")

# # Select the database
# mycursor.execute("USE mydatabase")
#
# # Create a table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#
# # Insert data into the table
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# # Commit the changes
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")
#
# # Retrieve data using the SELECT statement
# mycursor.execute("SELECT * FROM yourtable")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)
#
# # Alter data using the UPDATE statement
# sql = "UPDATE yourtable SET column1 = 'newvalue' WHERE id = 1"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) updated")

mydb.close()



