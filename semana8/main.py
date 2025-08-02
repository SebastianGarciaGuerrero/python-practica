import tkinter as tk
from tkinter import messagebox
from crud import agregar_videojuego, obtener_videojuegos, eliminar_videojuego, actualizar_videojuego

def guardar():
    agregar_videojuego(id_var.get(), titulo_var.get(), genero_var.get(), clasificacion_var.get(), plataforma_var.get())
    mostrar()
    limpiar()

def mostrar():
    lista.delete(0, tk.END)
    juegos = obtener_videojuegos()
    for juego in juegos:
        lista.insert(tk.END, juego)

def limpiar():
    id_var.set("")
    titulo_var.set("")
    genero_var.set("")
    clasificacion_var.set("")
    plataforma_var.set("")

def eliminar():
    eliminar_videojuego(id_var.get())
    mostrar()
    limpiar()

def actualizar():
    actualizar_videojuego(id_var.get(), titulo_var.get(), genero_var.get(), clasificacion_var.get(), plataforma_var.get())
    mostrar()
    limpiar()

root = tk.Tk()
root.title("Gestor de Videojuegos")

id_var = tk.StringVar()
titulo_var = tk.StringVar()
genero_var = tk.StringVar()
clasificacion_var = tk.StringVar()
plataforma_var = tk.StringVar()

tk.Label(root, text="ID").grid(row=0, column=0)
tk.Entry(root, textvariable=id_var).grid(row=0, column=1)

tk.Label(root, text="Título").grid(row=1, column=0)
tk.Entry(root, textvariable=titulo_var).grid(row=1, column=1)

tk.Label(root, text="Género").grid(row=2, column=0)
tk.Entry(root, textvariable=genero_var).grid(row=2, column=1)

tk.Label(root, text="Clasificación").grid(row=3, column=0)
tk.Entry(root, textvariable=clasificacion_var).grid(row=3, column=1)

tk.Label(root, text="Plataforma").grid(row=4, column=0)
tk.Entry(root, textvariable=plataforma_var).grid(row=4, column=1)

tk.Button(root, text="Guardar", command=guardar).grid(row=5, column=0)
tk.Button(root, text="Mostrar", command=mostrar).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=6, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=6, column=1)

lista = tk.Listbox(root, width=60)
lista.grid(row=7, column=0, columnspan=2)

root.mainloop()
