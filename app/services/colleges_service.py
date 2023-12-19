from app import mysql

def get_all_colleges():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM college")
    colleges_data = cursor.fetchall()

    cursor.close()

    return colleges_data



def add_college(college_code, college_name):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO college (collegeCode, collegeName) VALUES (%s, %s)",
            (college_code, college_name)
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error adding college: {e}")
        return False
    finally:
        if connection:
            connection.close()
            

def delete_college(college_code):
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("DELETE FROM college WHERE collegeCode = %s" , (college_code,))
    
    connection.commit()