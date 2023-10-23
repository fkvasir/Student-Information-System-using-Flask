# routes/students_bp.py
from flask import render_template, Blueprint, redirect, url_for
from models.students_m import get_students

students_bp = Blueprint('students_bp', __name__, template_folder='templates')

@students_bp.route('/')
def students_default():
    return redirect(url_for('students_bp.students_route'))

@students_bp.route('/students-list')
def students_route():
    students_data = get_students()
    return render_template('students.html', active_page='students', students_data=students_data)

# @students_bp.route('/add_students', methods=['POST'])
# def add_students():
#     student_id = request.form['studentID']
#     first_name = request.form['studentFname']
#     last_name = request.form['studentLname']
#     course = request.form['course']
#     year = request.form['year']
#     gender = request.form['gender']

#     # Connect to the database
#     conn = connect_to_database()
#     cursor = conn.cursor()

#     # Define the SQL query to insert a new student record
#     insert_query = "INSERT INTO students (student_id, first_name, last_name, course, year, gender) VALUES (%s, %s, %s, %s, %s, %s)"
#     values = (student_id, first_name, last_name, course, year, gender)

#     try:
#         cursor.execute(insert_query, values)
#         conn.commit()
#         flash('Student added successfully', 'success')
#     except Exception as e:
#         conn.rollback()
#         flash(f'Error adding student: {str(e)}', 'error')
#     finally:
#         cursor.close()
#         conn.close()

#     return redirect(url_for('students_bp.students_route'))
