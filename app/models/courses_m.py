from db.db_config import connect_to_database

def get_courses():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM course')
    courses_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return courses_data


# Set up routes
app.register_blueprint(students_bp, url_prefix='/')
app.register_blueprint(courses_bp, url_prefix='/')
app.register_blueprint(colleges_bp, url_prefix='/')

@app.route('/students/add', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        conn = connect_to_database()  # Use the function to connect

        cursor = conn.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO student (studentID, studentFname, studentLname, course, year, gender) " \
                       "VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (data["studentID"], data["studentFname"], data["studentLname"],
                                     data["course"], data["year"], data["gender"]))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"success": False, "error": str(e)})
    
@app.route('/colleges/add', methods=['POST'])
def add_college():
    try:
        data = request.get_json()
        conn = connect_to_database()  # Use the function to connect

        cursor = conn.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO college (collegeCode, collegeName)" \
                       "VALUES (%s, %s)"
        cursor.execute(insert_query, (data["collegeCode"], data["collegeName"]))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"success": False, "error": str(e)})
    
@app.route('/courses/add', methods=['POST'])
def add_course():
    try:
        data = request.get_json()
        conn = connect_to_database()  # Use the function to connect

        cursor = conn.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO student (courseCode, courseName, college) " \
                       "VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (data["courseCode"], data["courseName"], data["college"]))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"success": False, "error": str(e)})


# Index route
@app.route('/')
def index():
    return redirect('/students')

@app.route('/students/edit', methods=['PUT'])
def edit_student():
    try:
        data = request.get_json()
        conn = connect_to_database()
        cursor = conn.cursor()

        # Update the student data in the database
        update_query = "UPDATE student SET studentFname=%s, studentLname=%s, course=%s, year=%s, gender=%s WHERE studentID=%s"
        cursor.execute(update_query, (data["studentFname"], data["studentLname"], data["course"], data["year"], data["gender"], data["studentID"]))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"success": False, "error": str(e)})


@app.route('/students/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        delete_query = "DELETE FROM student WHERE studentID=%s"
        cursor.execute(delete_query, (student_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"success": False, "error": str(e)})


@app.route('/courses')
def courses():
    return render_template('courses.html', active_page='courses')
 
@app.route('/colleges')
def colleges():
    return render_template('college.html', active_page='colleges')