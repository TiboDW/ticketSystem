from flask import Flask
from markupsafe import escape
import sqlite3
import json




app = Flask(__name__)


#escape to prevent injection
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

#function get users 
@app.route("/users")
def getUser():
    connection = sqlite3.Connection("ticketSystem.db")
    cursor = connection.cursor()
    row = cursor.execute("SELECT * FROM user").fetchall()
    jsonString = json.dumps(row)
    print(jsonString)
    return jsonString 



#funciton to create comment


#funtion get all comments



#funtion get comment based on id
@app.route("/comment/<int:id>")
def getComment(id):
    connection = sqlite3.Connection("ticketSystem.db")
    cursor = connection.cursor()
    row = cursor.execute("SELECT * FROM comment WHERE userID = ?", (int(id),)).fetchall()
    #row = cursor.execute("SELECT * FROM comment").fetchall()
    jsonString = json.dumps(row)
    print(jsonString)
    return jsonString 

if __name__ == "__main__":
    app.run(debug=True)
