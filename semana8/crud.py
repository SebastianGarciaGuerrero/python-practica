from db_connection import get_connection

def agregar_videojuego(id, titulo, genero, clasificacion, plataforma):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id, titulo, genero, clasificacion, plataforma))
        conn.commit()
        conn.close()

def obtener_videojuegos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Videojuegos")
        return cursor.fetchall()

def eliminar_videojuego(id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Videojuegos WHERE ID = %s", (id,))
        conn.commit()
        conn.close()

def actualizar_videojuego(id, titulo, genero, clasificacion, plataforma):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE Videojuegos SET Titulo=%s, Genero=%s, Clasificacion=%s, Plataforma=%s WHERE ID=%s"
        cursor.execute(query, (titulo, genero, clasificacion, plataforma, id))
        conn.commit()
        conn.close()

def obtener_videojuegos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Videojuegos")
        return cursor.fetchall()
    else:
        return []

