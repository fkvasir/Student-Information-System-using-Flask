from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def students():
    return render_template('students.html')