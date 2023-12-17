
from flask import render_template, redirect
from app.services.students_service import get_all_students
from . import students

@students.route('/')
def index():
    return render_template('students.html')


@students.route('/students')
def show_students():
    students_data = get_all_students()
    return render_template('students.html', students_data=students_data)

