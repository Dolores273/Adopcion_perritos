import mysql.connector 
from mysql.connector import Error


DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root123",
    "database": "CentroAdopcion"
}

def get_db_connection():
    try:
        
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        
        print(f"Error conectando a la base de datos: {e}")
        return None