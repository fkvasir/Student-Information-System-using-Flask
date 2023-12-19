from app import mysql

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