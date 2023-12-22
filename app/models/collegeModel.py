from app import mysql

class College:
    @staticmethod
    def get_by_collegeName(college_name):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM college WHERE collegeName = %s"
        cursor.execute(query, (college_name,))
        college_data = cursor.fetchone()

        cursor.close()
        return college_data