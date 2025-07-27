import tkinter as tk
from tkinter import messagebox

def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    genero = genero_var.get()
    categorias = []
    if var_novela.get(): categorias.append("Novela")
    if var_ciencia.get(): categorias.append("Ciencia")
    if var_historia.get(): categorias.append("Historia")
    estado = estado_var.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = idioma_var.get()

    print("Título:", titulo)
    print("Autor:", autor)
    print("Año:", anio)
    print("Género:", genero)
    print("Categorías:", ", ".join(categorias))
    print("Estado:", estado)
    print("Copias:", copias)
    print("Resumen:", resumen)
    print("Idioma:", idioma)
    messagebox.showinfo("Éxito", "Libro registrado exitosamente")

def limpiar_formulario():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    genero_var.set(None)
    var_novela.set(False)
    var_ciencia.set(False)
    var_historia.set(False)
    estado_var.set(None)
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    idioma_var.set("Español")

root = tk.Tk()
root.title("Registro de Libros - SaberX")

frame_datos = tk.LabelFrame(root, text="Detalles del Libro")
frame_datos.pack(padx=10, pady=5)
tk.Label(frame_datos, text="Título:").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_datos)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_datos, text="Autor:").grid(row=1, column=0)
entry_autor = tk.Entry(frame_datos)
entry_autor.grid(row=1, column=1)

tk.Label(frame_datos, text="Año:").grid(row=2, column=0)
entry_anio = tk.Entry(frame_datos)
entry_anio.grid(row=2, column=1)

frame_genero = tk.LabelFrame(root, text="Género y Categoría")
frame_genero.pack(padx=10, pady=5)
genero_var = tk.StringVar()
tk.Radiobutton(frame_genero, text="Ficción", variable=genero_var, value="Ficción").pack(anchor="w")
tk.Radiobutton(frame_genero, text="No Ficción", variable=genero_var, value="No Ficción").pack(anchor="w")

var_novela = tk.BooleanVar()
var_ciencia = tk.BooleanVar()
var_historia = tk.BooleanVar()
tk.Checkbutton(frame_genero, text="Novela", variable=var_novela).pack(anchor="w")
tk.Checkbutton(frame_genero, text="Ciencia", variable=var_ciencia).pack(anchor="w")
tk.Checkbutton(frame_genero, text="Historia", variable=var_historia).pack(anchor="w")

frame_estado = tk.LabelFrame(root, text="Estado de Disponibilidad")
frame_estado.pack(padx=10, pady=5)
estado_var = tk.StringVar()
tk.Radiobutton(frame_estado, text="Disponible", variable=estado_var, value="Disponible").pack(anchor="w")
tk.Radiobutton(frame_estado, text="Prestado", variable=estado_var, value="Prestado").pack(anchor="w")

frame_copias = tk.LabelFrame(root, text="Copias Disponibles")
frame_copias.pack(padx=10, pady=5)
tk.Label(frame_copias, text="Número de copias:").pack()
entry_copias = tk.Entry(frame_copias)
entry_copias.pack()

frame_resumen = tk.LabelFrame(root, text="Resumen del Libro")
frame_resumen.pack(padx=10, pady=5)
text_resumen = tk.Text(frame_resumen, height=5, width=40)
text_resumen.pack()

idioma_var = tk.StringVar(value="Español")
menu_idioma = tk.OptionMenu(root, idioma_var, "Español", "Inglés")
menu_idioma.pack(padx=10, pady=5)

tk.Button(root, text="Registrar Libro", command=registrar_libro).pack(pady=5)
tk.Button(root, text="Limpiar", command=limpiar_formulario).pack(pady=5)

root.mainloop()
