from db.db_connection import connect_to_database

def get_colleges():
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM college')
    colleges_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return colleges_data
