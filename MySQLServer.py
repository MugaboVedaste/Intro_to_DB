import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mugabo$123",
    
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mydb.commit()
    print(f"Database \'alx_book_store\' created successfully!")
except mysql.connector.Error:
    print(f"Didn't connected")
    

mycursor.close()
mydb.close()