from flask import Flask, render_template, redirect
from routes.student_bp import students_bp
from routes.college_bp import colleges_bp
from routes.course_bp import courses_bp
import mysql.connector
from db.db_config import db_config

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/students')

def connect_to_database():
    return mysql.connector.connect(**db_config)

app.register_blueprint(students_bp, url_prefix='/students')
app.register_blueprint(courses_bp, url_prefix='/courses')
app.register_blueprint(colleges_bp, url_prefix='/colleges')

if __name__ == '__main__':
    app.run(debug=True)
