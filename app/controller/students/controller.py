from flask import render_template
from app.services.students_service import get_all_students
from . import students

@students.route('/students')
def show_students():
    students_data = get_all_students()
    return render_template('students.html', students_data=students_data)

