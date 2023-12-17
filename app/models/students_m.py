from db.db_config import connect_to_database

def get_students():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM student')
    students_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return students_data

def update_student(studentID, studentFname, studentLname, course, year, gender):
    try:
        conn = connect_to_database()  # Use the function to connect

        cursor = conn.cursor()

        # Update data in the database
        update_query = "UPDATE student SET studentFname = %s, studentLname = %s, course = %s, year = %s, gender = %s WHERE studentID = %s"
        cursor.execute(update_query, (studentFname, studentLname, course, year, gender, studentID))
        conn.commit()

        cursor.close()
        conn.close()

        return True

    except Exception as e:
        print("Error:", str(e))
        return False
