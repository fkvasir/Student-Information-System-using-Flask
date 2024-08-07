# courses_service.py
from app import mysql
from app.models.coursesModel import Course


def get_all_courses():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM course ORDER BY createdAt DESC")
    courses_data = cursor.fetchall()

    cursor.close()

    return courses_data


def add_course(course_code, course_name, college):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO course (courseCode, courseName, college) VALUES (%s, %s, %s)",
            (course_code, course_name, college)
        )
        
        connection.commit()
        cursor.close()
        return True
    
    except Exception as e:
        print(f"Error adding course: {e}")
        return False
    
    finally:
        if connection:
            connection.close()

            
            
def delete_course(courseCode):
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("DELETE FROM course WHERE courseCode = %s" , (courseCode,))
    
    connection.commit()







def update_course(course_code, course_name, college):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        print('Updating course:', course_code, course_name, college)
        query = "UPDATE course SET courseName = %s, college = %s WHERE courseCode = %s"
        print('Query:', query)
        cursor.execute(query, (course_name, college, course_code))
        connection.commit()
        return True
    
    except Exception as e:
        print(f"Error updating course: {str(e)}")
        connection.rollback()
        return False
    
    finally:
        cursor.close()

    
    
def search_courses(query):
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    search_query = "SELECT * FROM course WHERE courseCode LIKE %s OR courseName LIKE %s"
    cursor.execute(search_query, ('%' + query + '%', '%' + query + '%'))

    courses_data = cursor.fetchall()
    cursor.close()

    return courses_data