import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mugabo$123",
    
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
mydb.commit()
print(f"Database \'alx_book_store\' created successfully!")
mycursor.close()
mydb.close()