import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="clinica",
            user="root",
            password="mysqlpass",
            port=3307
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos 'clinica'")
            return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Función para probar la conexión
def test_connection():
    conn = get_connection()
    if conn:
        conn.close()

if __name__ == '__main__':
    test_connection()