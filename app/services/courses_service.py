from app import mysql

def get_all_courses():
    connection = mysql.connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM course")
    courses_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return courses_data
