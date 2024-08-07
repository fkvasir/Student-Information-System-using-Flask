from app import mysql
from .collegeModel import College

class Student:
    @staticmethod
    def get_by_id(student_id):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM student WHERE studentID = %s"
        cursor.execute(query, (student_id,))
        student_data = cursor.fetchone()

        cursor.close()
        return student_data
    
    @staticmethod
    def get_with_college_by_id(student_id):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT 
                student.studentID, 
                student.studentFname, 
                student.studentLname, 
                student.year, 
                student.gender, 
                student.profile_picture,
                course.courseCode, 
                course.courseName, 
                college.collegeCode, 
                college.collegeName
            FROM student
            LEFT JOIN course ON student.course = course.courseCode
            LEFT JOIN college ON course.college = college.collegeCode
            WHERE student.studentID = %s
        """
        cursor.execute(query, (student_id,))
        student_data_with_college = cursor.fetchone()

        cursor.close()
        return student_data_with_college
    
    
    @staticmethod
    def search_students(query, criteria):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        search_query = f"SELECT * FROM student WHERE {criteria} LIKE %s"
        like_query = '%' + query + '%'

        cursor.execute(search_query, (like_query,))
        students_data = cursor.fetchall()
        cursor.close()

        return students_data

