
from flask import render_template
from app.services.courses_service import get_all_courses
from . import courses

@courses.route('/courses')
def show_courses():
    courses_data = get_all_courses()
    return render_template('courses.html', courses_data=courses_data)
