from app import mysql

class Course:
    @staticmethod
    def get_by_code(course_code):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM course WHERE courseCode = %s"
        cursor.execute(query, (course_code,))
        course_data = cursor.fetchone()

        cursor.close()
        return course_data
    
    
    @staticmethod
    def get_all_courses():
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT courseCode, courseName FROM course"
        cursor.execute(query)
        courses = cursor.fetchall()

        cursor.close()
        return courses