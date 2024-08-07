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
    
    def search_course(query, criteria):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)
        
        search_query = f"SELECT * FROM course WHERE {criteria} LIKE %s"
        like_query = '%' + query + '%'
        cursor.execute(search_query, (like_query,))
        data = cursor.fetchall()
        cursor.close()
        
        return data