
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.courses_service import get_all_courses, add_course, delete_course, update_course
from . import courses
from app.models.coursesModel import Course
from app import mysql
from app.models.collegeModel import College


@courses.route('/courses')
def show_courses():
    courses_data = get_all_courses()
    return render_template('courses.html', courses_data=courses_data)

@courses.route('/courses/add', methods=['GET', 'POST'])
def add_course_form():
    if request.method == 'POST':
        course_code = request.form.get('courseCode')
        course_name = request.form.get('courseName')
        college = request.form.get('college')
        
        print(f"Received data: Course Code - {course_code}, Course Name - {course_name}, College - {college}")
        
        try:
            add_course(course_code, course_name, college)
            return jsonify({'status': 'success', 'message': 'Course added successfully!'})
        except Exception as e:
            print(f"Error adding course: {e}")
            return jsonify({'status': 'error', 'message': str(e)})

    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM college")
    colleges_data = cursor.fetchall()

    return render_template('add_course.html', colleges_data=colleges_data)





@courses.route('/courses/delete/<string:courseCode>', methods=['DELETE'])
def delete_course_route(courseCode):
    try:

        delete_course(courseCode)
        response = {'status': 'success', 'message': 'Course deleted successfully!'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    return jsonify(response)


@courses.route('/courses/update', methods=['POST'])
def update_course_route():
    try:
        data = request.get_json()  
        course_code = data.get('editCourseCode') 
        course_name = data.get('editCourseName')
        college = data.get('editCollege')

        success = update_course(course_code,course_name , college)
        if success:
            return jsonify({'message': 'Courses updated successfully'}), 200
        else:
            return jsonify({'error': 'Error updating course'}), 500
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred. Please try again.'}), 500


@courses.route('/colleges/get_college', methods=['GET'])
def get_college():
    try:
        college = College.get_all_college()
        return jsonify(college), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred. Please try again.'}), 500