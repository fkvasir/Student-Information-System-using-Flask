from flask import Flask, render_template, request, redirect
import mysql.connector
from db.db_config import db_config

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(**db_config)

@app.route('/add_college', methods=['POST'])
def add_college():
    conn = connect_to_database()
    cursor = conn.cursor()

    code = request.form.get('code')
    name = request.form.get('name')

    add_college_query = "INSERT INTO college (code, name) VALUES (%s, %s)"
    cursor.execute(add_college_query, (code, name))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/colleges')

if __name__ == '__main__':
    app.run(debug=True)
