from flask import render_template, Blueprint
from models.courses_m import get_courses

courses_bp = Blueprint('courses_bp', __name__)

@courses_bp.route('/courses')
def courses_route():
    courses_data = get_courses()
    return render_template('courses.html', active_page='courses', courses_data=courses_data)
