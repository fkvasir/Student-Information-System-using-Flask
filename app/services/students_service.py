from app import mysql

def get_all_students():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM student")
    students_data = cursor.fetchall()

    cursor.close()

    return students_data
