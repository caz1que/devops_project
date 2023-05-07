from flask import Flask, render_template

app = Flask(__name__)

import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='192.168.1.98', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM Users')
students = cursor.fetchall()
connection.close()

@app.route('/')
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")



