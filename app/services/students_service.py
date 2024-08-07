from app import mysql
import cloudinary.uploader
from app.models.studentsModel import Student


def get_all_students():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM student ORDER BY studentLname ASC")
    students_data = cursor.fetchall()

    cursor.close()

    return students_data


def add_student(student_id, student_fname, student_lname, course, year, gender, profile_picture):
    try:
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO student (studentID, studentFname, studentLname, course, year, gender, profile_picture) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (student_id, student_fname, student_lname, course, year, gender, profile_picture)
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
    
    


def update_student(student_id, student_fname, student_lname, course, year, gender):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        print('Updating student:', student_id, student_fname, student_lname, course, year, gender)
        query = "UPDATE student SET studentFname = %s, studentLname = %s, course = %s, year = %s, gender = %s WHERE studentID = %s"
        print('Query:', query)
        cursor.execute(query, (student_fname, student_lname, course, year, gender, student_id))
        connection.commit()
        return True
    
    except Exception as e:
        print(f"Error updating student: {str(e)}")
        connection.rollback()
        return False
    
    finally:
        cursor.close()

def get_courseCode():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT course_code FROM course"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def check_student_ID(student_ID):
    cursor = mysql.connection.cursor()
    query = "SELECT ID FROM student where ID = %s"
    cursor.execute(query, (student_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_student_info(student_ID):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM student where ID = %s"
    cursor.execute(query, (student_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result


def search_students(query):
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    search_query = (
        "SELECT * FROM student WHERE "
        "studentID LIKE %s OR "
        "studentFname LIKE %s OR "
        "studentLname LIKE %s OR "
        "gender LIKE %s OR "
        "course LIKE %s"
    )

    like_query = '%' + query + '%'

    cursor.execute(search_query, (like_query, like_query, like_query, like_query, like_query))

    students_data = cursor.fetchall()
    cursor.close()

    return students_data


def search_students(query):
    return Student.search(query)
