from app import mysql

def get_all_students():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM student")
    students_data = cursor.fetchall()

    cursor.close()

    return students_data


def add_student(student_id, student_fname, student_lname, course, year, gender):
    try:
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO student (studentID, studentFname, studentLname, course, year, gender) VALUES (%s, %s, %s, %s, %s, %s)",
            (student_id, student_fname, student_lname, course, year, gender)
        )

        connection.commit()

        cursor.close()

        return True  

    except Exception as e:
        print(f"Error adding student: {e}")
        return False  

    finally:
        if connection:
            connection.close()

def delete_student(studentID):
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("DELETE FROM student WHERE studentID = %s" , (studentID,))
    
    connection.commit()