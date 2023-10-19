from flask import Blueprint, render_template

college_bp = Blueprint('student', __name__, template_folder='templates')

@college_bp.route('/')
def students():
    return render_template('students.html', active_page='student')

@college_bp.route('/colleges')
def colleges():
    return render_template('college.html', active_page='college')

@college_bp.route('/courses')
def courses():
    return render_template('courses.html', active_page='courses')



