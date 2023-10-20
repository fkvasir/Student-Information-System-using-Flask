# routes/colleges.py
from flask import render_template, Flask
from models.courses_m import get_courses

app = Flask(__name__)

@app.route('/courses')
def courses():
    courses_data = get_courses()
    return render_template('courses.html', active_page='courses', courses_data=courses_data)
