
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.colleges_service import get_all_colleges
from . import colleges
from app.services.colleges_service import add_college, delete_college, update_college
from ...models.collegeModel import College
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
        
        if not college_code or not college_name:
            return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400 
        
        try:
            add_college(college_code, college_name)
            return jsonify({'status': 'success', 'message': 'College added successfully!'})
        except Exception as e:
            print(f"Error adding college: {e}")
            return jsonify({'status': 'error', 'message': str(e)})

    return render_template('add_college.html')




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


   
