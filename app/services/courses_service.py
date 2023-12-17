# courses_service.py
from app import mysql

def get_all_courses():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM course")
    courses_data = cursor.fetchall()

    cursor.close()

    return courses_data
