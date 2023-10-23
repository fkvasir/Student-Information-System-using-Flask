from flask import Flask, render_template, redirect, Blueprint
from routes.students_bp import students_bp
from routes.colleges_bp import colleges_bp
from routes.courses_bp import courses_bp
import mysql.connector
from db.db_config import db_config

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(**db_config)

# Set up routes
app.register_blueprint(students_bp, url_prefix='/')
app.register_blueprint(courses_bp, url_prefix='/')
app.register_blueprint(colleges_bp, url_prefix='/colleges')

# Index route
@app.route('/')
def index():
    return redirect('/students')


@app.route('/courses')
def courses():
    return render_template('courses.html', active_page='courses')

@app.route('/colleges')
def colleges():
    return render_template('college.html', active_page='colleges')

if __name__ == '__main__':
    app.run(debug=True)