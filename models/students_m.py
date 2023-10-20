from db.db_connection import connect_to_database

def get_students():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM student')
    students_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return students_data
