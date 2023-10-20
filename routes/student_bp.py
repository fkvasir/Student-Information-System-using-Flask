# routes/colleges.py
from flask import render_template
from models.students_m import get_students

app = Flask(__name__)

@app.route('/students')
def students():
    students_data = get_students()
    return render_template('students.html', active_page='students', students_data=students_data)
