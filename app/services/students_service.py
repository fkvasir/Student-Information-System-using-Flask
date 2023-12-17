from app import mysql

def get_all_students():
    connection = mysql.connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM student")
    students_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return students_data
