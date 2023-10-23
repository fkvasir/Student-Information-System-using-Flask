from flask import render_template, Blueprint, redirect, url_for
from models.courses_m import get_courses

courses_bp = Blueprint('courses_bp', __name__, template_folder='templates')

@courses_bp.route('/')
def courses_default():
    return redirect(url_for('courses_bp.courses_route'))

@courses_bp.route('/courses-list')
def courses_route():
    courses_data = get_courses()
    return render_template('courses.html', active_page='courses', courses_data=courses_data)
