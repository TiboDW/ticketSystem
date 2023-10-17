import sqlite3
import json

#this file is purely to create a db
connection = sqlite3.connect("ticketSystem.db");

cursor = connection.cursor();

#create table user
cursor.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, admin BOOLEAN NOT NULL)")

#create table comments
cursor.execute("CREATE TABLE comment (id INTEGER PRIMARY Key, userID INTEGER NOT NULL, name VARCHAR(255) NOT NULL, comment VARCHAR(255))")

#insert users
cursor.execute("INSERT INTO user(name, password, admin) VALUES ('Jan', 'jan123', true)")
cursor.execute("INSERT INTO user(name, password, admin) VALUES ('Pieter', 'pieter123', false)")
cursor.execute("INSERT INTO user(name, password, admin) VALUES ('Jos', 'jos123', false)")

#insert comment
cursor.execute("INSERT INTO comment(userID, name, comment) VALUES ('1', 'fout systeem', 'er is een fout in het systeem')")



#check for correct input of the tables
print(connection.total_changes)
print("table user")
jsonString = json.dumps(cursor.execute("SELECT * From user").fetchall())
print("json")
print(jsonString)
print("normal")
print(cursor.execute("SELECT * From user").fetchall())
print("table comment")
print(cursor.execute("SELECT * From comment WHERE userID = 1").fetchall())

connection.commit()
connection.close()