from app import mysql

def get_all_colleges():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM college ORDER BY createdAt DESC")
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
    
    
    
def update_college(college_code, college_name):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        print('Updating college:', college_code, college_name)
        query = "UPDATE college SET collegeName = %s WHERE collegeCode = %s"
        print('Query:', query)
        cursor.execute(query, (college_name, college_code))
        connection.commit()
        return True
    
    except Exception as e:
        print(f"Error updating college: {str(e)}")
        connection.rollback()
        return False
    
    finally:
        cursor.close()

def search_colleges(query):
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    search_query = "SELECT * FROM college WHERE collegeCode LIKE %s OR collegeName LIKE %s"
    cursor.execute(search_query, ('%' + query + '%', '%' + query + '%'))

    colleges_data = cursor.fetchall()
    cursor.close()

    return colleges_data