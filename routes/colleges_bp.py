from flask import render_template, Blueprint, redirect, url_for
from models.colleges_m import get_colleges

colleges_bp = Blueprint('colleges_bp', __name__, template_folder='templates')

@colleges_bp.route('/')
def colleges_default():
    return redirect(url_for('colleges_bp.colleges_route'))

@colleges_bp.route('/colleges-list')
def colleges_route():
    colleges_data = get_colleges()
    return render_template('college.html', active_page='colleges', colleges_data=colleges_data)
