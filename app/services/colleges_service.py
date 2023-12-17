from app import mysql

def get_all_colleges():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM college")
    colleges_data = cursor.fetchall()

    cursor.close()

    return colleges_data

