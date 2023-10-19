from flask import Flask, render_template, Blueprint, redirect
from routes.student_bp import student_bp
import mysql.connector
from db.db_config import db_config


app = Flask(__name__)


def connect_to_database():
    return mysql.connector.connect(**db_config)


@app.route('/')
def index():
    return redirect('/students')

@app.route('/courses')
def courses():
    return render_template('courses.html', active_page='courses')

@app.route('/colleges')
def colleges():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM college')
    colleges_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('college.html', active_page='colleges', colleges_data=colleges_data)

app.register_blueprint(student_bp, url_prefix='/students')

if __name__ == '__main__':
    app.run(debug=True)
