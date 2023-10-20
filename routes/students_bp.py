from flask import render_template, Blueprint
from models.students_m import get_students

students_bp = Blueprint('students_bp', __name__)

@students_bp.route('/')
def students_route():
    students_data = get_students()
    return render_template('students.html', active_page='students', students_data=students_data)
