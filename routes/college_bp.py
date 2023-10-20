# routes/colleges_bp.py
from flask import render_template, Blueprint
from models.college_m import get_colleges

colleges_bp = Blueprint('college_bp', __name__)

@colleges_bp.route('/colleges')
def colleges_route():
    colleges_data = get_colleges()
    return render_template('college.html', active_page='colleges', colleges_data=colleges_data)
