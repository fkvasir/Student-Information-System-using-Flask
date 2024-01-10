
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.students_service import get_all_students
from . import students
from app.services.students_service import add_student, delete_student, update_student
from app.models.studentsModel import Student
from app import mysql


@students.route('/')
def index():
    return render_template('students.html')


@students.route('/students')
def show_students():
    students_data = get_all_students()
    return render_template('students.html', students_data=students_data)

@students.route('/students/add', methods=['GET', 'POST'])
def add_student_form():
    if request.method == 'POST':
        student_id = request.form.get('studentID')
        student_fname = request.form.get('studentFname')
        student_lname = request.form.get('studentLname')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')
        
        try:
            add_student(student_id, student_fname, student_lname, course, year, gender )
            return jsonify({'status': 'success', 'message': 'Student added successfully!'})
        except Exception as e:
            print(f"Error adding student: {e}")
            return jsonify({'status': 'error', 'message': str(e)})

    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM course")
    courses_data = cursor.fetchall()

    return render_template('add_student.html', courses_data=courses_data)

        



@students.route('/students/delete/<string:studentID>', methods=['DELETE'])
def delete_student_route(studentID):
    try:

        delete_student(studentID)
        response = {'status': 'success', 'message': 'Student deleted successfully!'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    return jsonify(response)



@students.route('/students/profile/<string:studentID>')
def show_student_profile(studentID):
    student_data_with_college = Student.get_with_college_by_id(studentID)
    print(student_data_with_college)
    return render_template('student_profile.html', student_data=student_data_with_college, college_data=student_data_with_college)


@students.route('/students/update', methods=['POST'])
def update_student_route():
    try:
        student_id = request.json.get('editStudentId')
        student_fname = request.json.get('editStudentFName')
        student_lname = request.json.get('editStudentLName')
        course = request.json.get('editCourse')
        year = request.json.get('editYear')
        gender = request.json.get('editGender')

        print('Received data:', student_id, student_fname, student_lname, course, year, gender)

        success = update_student(student_id, student_fname, student_lname, course, year, gender)

        if success:
            return jsonify({'message': 'Student updated successfully'}), 200
        else:
            return jsonify({'error': 'Error updating student'}), 500
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred. Please try again.'}), 500
