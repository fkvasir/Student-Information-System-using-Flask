
import mysql.connector
from db.db_config import db_config

def connect_to_database():
    return mysql.connector.connect(**db_config)
