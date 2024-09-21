from flask import render_template, redirect, request, url_for, jsonify, flash, Blueprint
from app.services.students_service import get_all_students
from . import students
from app.services.students_service import add_student, delete_student, update_student
from app.models.studentsModel import Student
from app.models.collegeModel import College
from app import mysql
from app.models.coursesModel import Course
from app.services.cloudinary_service import upload_image
from app.services.courses_service import get_all_courses
import re


@students.route('/')
def index():
    return redirect(url_for('students.show_students'))


@students.route('/students')
def show_students():
    students_data = get_all_students()
    courses_data = get_all_courses()  # Fetch all courses
    return render_template('students.html', students_data=students_data, courses_data=courses_data)

@students.route('/students/add', methods=['GET', 'POST'])
def add_student_form():
    if request.method == 'POST':
        student_id = request.form.get('studentID')
        if not re.match(r'^\d{4}-\d{4}$', student_id):
            return jsonify ({'status': 'error', 'message': 'Invalid ID format.'}),
        student_fname = request.form.get('studentFname')
        student_lname = request.form.get('studentLname')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')
        profile_picture = request.form.get('profile_picture')

        print(f"Profile picture URL: {profile_picture}")  # Debugging line
        
        # Validate required fields
        if not student_id or not student_fname or not student_lname or not course or not year or not gender:
            return jsonify({'status': 'error', 'message': 'All fields are required!'}), 400

        # Check if studentID already exists
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student WHERE studentID = %s", (student_id,))
        existing_student = cursor.fetchone()
        
        if existing_student:
            cursor.close()
            return jsonify({'status': 'error', 'message': 'Student ID already exists!'}), 400
        
        try:
            # Assuming you have a function to add the student
            add_student(student_id, student_fname, student_lname, course, year, gender, profile_picture)
            cursor.close()
            return jsonify({'status': 'success', 'message': 'Student added successfully!'})
        except Exception as e:
            print(f"Error adding student: {e}")
            cursor.close()
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course")
        courses_data = cursor.fetchall()

        student_id = request.args.get('id')
        student_data = None
        if student_id:
            # Fetch student data if id is provided
            cursor.execute("SELECT * FROM student WHERE studentID = %s", (student_id,))
            student_data = cursor.fetchone()

        cursor.close()

        return render_template('add_student.html', courses_data=courses_data, student_data=student_data)
    

@students.route('/students/check_duplicate/<student_id>', methods=['GET'])
def check_duplicate(student_id):
    try:
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT 1 FROM student WHERE studentID = %s", (student_id,))
        exists = cursor.fetchone() is not None
        cursor.close()
        
        return jsonify({'exists': exists})
    except Exception as e:
        print(f"Error checking for duplicate student ID: {e}")
        return jsonify({'exists': False, 'error': str(e)}), 500    



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

@students.route('/courses/get_courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.get_all_courses()
        return jsonify(courses), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred. Please try again.'}), 500


@students.route('/upload_student_image', methods=['POST'])
def upload_student_image():
    if 'image' not in request.files or 'student_id' not in request.form:
        return jsonify({'error': 'Missing image or student ID'}), 400
    
    image_file = request.files['image']
    student_id = request.form['student_id']
    
    try:
        image_url = upload_image(image_file.stream)
        if image_url:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("UPDATE student SET profile_picture = %s WHERE studentID = %s", (image_url, student_id))
            conn.commit()
            cursor.close()
            return jsonify({'status': 'success', 'message': 'Profile picture updated successfully!'}), 200
        else:
            return jsonify({'error': 'Image upload failed'}), 500
    except Exception as e:
        print(f"Database update error: {e}")
        return jsonify({'error': 'Failed to update profile picture in the database'}), 500
    
    
@students.route('/students/update_profile_picture', methods=['POST'])
def update_profile_picture():
    if request.method == 'POST':
        data = request.get_json()
        student_id = data.get('studentID')
        profile_picture = data.get('profile_picture')
        print("Updating STudent Iamge", student_id, profile_picture)

        try:
            connection = mysql.connection
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE student SET profile_picture = %s WHERE studentID = %s",
                (profile_picture, student_id)
            )
            connection.commit()
            cursor.close()
            return jsonify({'status': 'success', 'message': 'Profile picture updated successfully!'})
        except Exception as e:
            print(f"Error updating profile picture: {e}")
            return jsonify({'status': 'error', 'message': str(e)})
        finally:
            if connection:
                connection.close()



@students.route('/search', methods=['GET'])
def search_students():
    query = request.args.get('query')
    option = request.args.get('option')
    criteria = request.args.get('criteria')
    print("hello",query, option, criteria)

    if not query or not criteria:
        return jsonify({'status': 'error', 'message': 'Invalid search parameters'})
    
    if option == 'student':
        data = Student.search_students(query, criteria)
        return render_template('search_results.html', students_data=data)
    elif option == 'colleges':
        data = College.search_colleges(query, criteria)
        return render_template('search_results_colleges.html', college_data=data)
    else:
        data = Course.search_course(query,criteria)
        return render_template('search_results_course.html', course_data=data)
        
