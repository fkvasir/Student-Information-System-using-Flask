from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__, template_folder='templates')

@student_bp.route('/')
def students():
    return render_template('students.html', active_page='student')

@student_bp.route('/colleges')
def colleges():
    return render_template('college.html', active_page='college')

