from app import mysql

class College:
    @staticmethod
    def get_by_collegecode(college_code):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM college WHERE collegeCode = %s"
        cursor.execute(query, (college_code,))
        college_data = cursor.fetchone()

        cursor.close()
        return college_data