from flask import Flask, render_template, redirect, Blueprint
from routes.student_bp import students_bp
from routes.college_bp import colleges_bp
from routes.courses_bp import courses_bp
import mysql.connector
from db.db_config import db_config

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return redirect('/students')

@app.route('/courses_page')  # Renamed route to avoid conflicts
def courses_page():
    return render_template('courses.html', active_page='courses')

app.register_blueprint(students_bp, url_prefix='/students')
app.register_blueprint(courses_bp, url_prefix='/courses')
app.register_blueprint(colleges_bp, url_prefix='/colleges')

if __name__ == '__main__':
    app.run(debug=True)
