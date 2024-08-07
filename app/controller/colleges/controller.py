
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.colleges_service import get_all_colleges
from . import colleges
from app.services.colleges_service import add_college, delete_college, update_college
from ...models.collegeModel import College
from app import mysql
import cloudinary

@colleges.route('/colleges')
def show_colleges():
    college_data = get_all_colleges() 
    print(college_data)
    return render_template('college.html', college_data=college_data)



@colleges.route('/colleges/add', methods=['GET', 'POST'])
def add_college_form():
    if request.method == 'POST':
        college_code = request.form.get('collegeCode')
        college_name = request.form.get('collegeName')


        # Validate required fields
        if not college_code or not college_name:
            return jsonify({'status': 'error', 'message': 'All fields are required!'}), 400

        # Check if collegeCode already exists
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM college WHERE collegeCode = %s", (college_code,))
        existing_college = cursor.fetchone()

        if existing_college:
            cursor.close()
            return jsonify({'status': 'error', 'message': 'College Code already exists!'}), 400

        try:
            # Add College
            add_college(college_code, college_name)
            cursor.close()
            return jsonify({'status': 'success', 'message': 'College added successfully!'})
        except Exception as e:
            print(f"Error adding College: {e}")
            cursor.close()
            return jsonify({'status': 'error', 'message': str(e)}), 500

    college_code = request.args.get('code')
    college_data = None
    if college_code:
        cursor.execute("SELECT * FROM college WHERE collegeCode = %s", (college_code,))
        college_data = cursor.fetchone()


    return render_template('add_college.html', college_data=college_data)
    

@colleges.route('/courses/check_duplicate/<college_code>', methods=['GET'])
def check_duplicate(college_code):
    try:
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT 1 FROM college WHERE collegeCode = %s", (college_code,))
        exists = cursor.fetchone() is not None
        cursor.close()
        
        return jsonify({'exists': exists})
    except Exception as e:
        print(f"Error checking for duplicate College Code: {e}")
        return jsonify({'exists': False, 'error': str(e)}), 500    

@colleges.route('/colleges/delete/<string:collegeCode>', methods=['DELETE'])
def delete_college_route(collegeCode):
    try:

        delete_college(collegeCode)
        response = {'status': 'success', 'message': 'College deleted successfully!'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    return jsonify(response)



@colleges.route('/colleges/update', methods=['POST'])
def update_college_route():
    try:
        data = request.get_json()  
        college_code = data.get('editCollegeCode')  # Assuming the key is 'editCollegeCode'
        college_name = data.get('editCollegeName')

        success = update_college(college_code, college_name)
        if success:
            return jsonify({'message': 'College updated successfully'}), 200
        else:
            return jsonify({'error': 'Error updating college'}), 500
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred. Please try again.'}), 500


   
