
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.courses_service import get_all_courses, add_course, delete_course
from . import courses
from app.models.coursesModel import Course
from app import mysql


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