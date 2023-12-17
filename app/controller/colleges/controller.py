from flask import render_template
from app.services.colleges_service import get_all_colleges
from . import colleges

@colleges.route('/colleges')
def show_colleges():
    colleges_data = get_all_colleges()
    return render_template('colleges.html', colleges_data=colleges_data)

