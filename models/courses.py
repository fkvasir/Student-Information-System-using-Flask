# models/college.py
from db.db_connection import connect_to_database

def get_courses():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM courses')
    courses_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return courses_data
