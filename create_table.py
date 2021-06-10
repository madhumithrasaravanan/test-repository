import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"

cursor.execute(create_table)

create_table2="CREATE TABLE IF NOT EXISTS item(id INTEGER PRIMARY KEY,name text,price float)"

cursor.execute(create_table2)


connection.commit()
connection.close()