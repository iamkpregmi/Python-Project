#python -m pip install mysql-connector-python
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
######################################################################################
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("select * from emp")

for x in mycursor:
  print(x)