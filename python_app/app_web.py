from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

connection = mysql.connector.connect(user='root', password=os.getenv('db_root_password'), host=os.getenv('MYSQL_SERVICE_HOST', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM Users')
users = cursor.fetchall()
connection.close()

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")



