from app import mysql

def get_all_colleges():
    connection = mysql.connect()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM college")
    colleges_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return colleges_data
