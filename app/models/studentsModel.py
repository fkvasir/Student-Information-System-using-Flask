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
            SELECT student.*, course.courseCode, college.collegeCode
            FROM student
            LEFT JOIN course ON student.course = course.courseCode
            LEFT JOIN college ON course.college = college.collegeCode
            WHERE student.studentID = %s
        """
        cursor.execute(query, (student_id,))
        student_data_with_college = cursor.fetchone()

        cursor.close()
        return student_data_with_college



