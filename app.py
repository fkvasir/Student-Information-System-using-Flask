from flask import Flask, render_template, Blueprint, redirect
from routes.student_bp import students
from routes.college_bp import colleges
from routes.courses_bp import courses
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

app.register_blueprint(students, url_prefix='/students')
app.register_blueprint(courses, url_prefix='/courses')
app.register_blueprint(colleges, url_prefix='/colleges')


if __name__ == '__main__':
    app.run(debug=True)
