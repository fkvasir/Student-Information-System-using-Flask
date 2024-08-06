from app import mysql

class College:
    @staticmethod
    def get_by_collegeName(college_name):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM college WHERE collegeName = %s"
        cursor.execute(query, (college_name))
        college_data = cursor.fetchone()

        cursor.close()
        return college_data
    
    @staticmethod
    def get_all_college():
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT collegeCode, collegeName FROM college"
        cursor.execute(query)
        college = cursor.fetchall()

        cursor.close()
        return college
        