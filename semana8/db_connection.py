import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysqlpass',
            database='videojuegos_db',
            port=3307
        )
        return conn
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
