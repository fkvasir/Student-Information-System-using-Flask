import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
SECRET_KEY = os.getenv("SECRET_KEY")


def run_schema_sql(file):
    try:
        connection = mysql.connector.connect(
            user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME
        )

        cursor = connection.cursor()

        with open(file, "r") as sql_file:
            sql_commands = sql_file.read().split(";")

            for sql_command in sql_commands:
                if sql_command.strip():
                    cursor.execute(sql_command)
                    connection.commit()

            print("Database Initialized. File Executed Successfully!")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    file = "schema.sql"
    run_schema_sql(file)
