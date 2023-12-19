
from flask import render_template, redirect, request, url_for, jsonify, flash
from app.services.colleges_service import get_all_colleges
from . import colleges
from app.services.colleges_service import add_college, delete_college


@colleges.route('/colleges')
def show_colleges():
    colleges_data = get_all_colleges()
    return render_template('college.html', colleges_data=colleges_data)



@colleges.route('/colleges/add', methods=['GET', 'POST'])
def add_college_form():
    if request.method == 'POST':
        college_code = request.form.get('collegeCode')
        college_name = request.form.get('collegeName')
        
        
        
        add_college(college_code, college_name)
        return redirect(url_for('colleges.show_colleges'))
        
        # return redirect('college.html')

    return render_template('add_college.html')




@colleges.route('/colleges/delete/<string:collegeCode>', methods=['DELETE'])
def delete_course_route(collegeCode):
    try:

        delete_college(collegeCode)
        response = {'status': 'success', 'message': 'College deleted successfully!'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    return jsonify(response)