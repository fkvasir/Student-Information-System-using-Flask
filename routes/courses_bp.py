from flask import Blueprint, render_template

courses_bp = Blueprint('student', __name__, template_folder='templates')

@courses_bp.route('/')
def students():
    return render_template('students.html', active_page='student')

@courses_bp.route('/colleges')
def colleges():
    return render_template('college.html', active_page='college')

@courses_bp.route('/colleges')
def courses():
    return render_template('courses.html', active_page='courses')

