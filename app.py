from flask import Flask, render_template

app = Flask(__name__)
app.static_folder='static'

@app.route('/')
def students():
    return render_template('students.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/colleges')
def colleges():
    return render_template('college.html')

if __name__ == '__main__':
    app.run(debug=True)