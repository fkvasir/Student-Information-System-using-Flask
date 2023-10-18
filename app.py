from flask import Flask, render_template, Blueprint, redirect
from routes.student_bp import student_bp

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/students')

@app.route('/courses')
def courses():
    return render_template('courses.html', active_page='courses')

@app.route('/colleges')
def colleges():
    return render_template('college.html', active_page='college')

app.register_blueprint(student_bp, url_prefix='/students')

if __name__ == '__main__':
    app.run(debug=True)