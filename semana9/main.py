import tkinter as tk
from tkinter import ttk, messagebox

# Importar las funciones correctas desde crud.py
from crud import agregar_pacientes, obtener_pacientes, eliminar_paciente, actualizar_paciente

class PacientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.geometry("950x500")

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Variables de entrada
        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.genero_var = tk.StringVar()
        self.historial_var = tk.StringVar()
        self.contacto_var = tk.StringVar()

        # Widgets de entrada
        campos = [
            ("ID Paciente:", self.id_var),
            ("Nombre:", self.nombre_var),
            ("Edad:", self.edad_var),
            ("Género:", self.genero_var),
            ("Historial Médico:", self.historial_var),
            ("Contacto:", self.contacto_var)
        ]

        for i, (label, var) in enumerate(campos):
            ttk.Label(self.frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            ttk.Entry(self.frame, textvariable=var).grid(row=i, column=1, sticky=(tk.W, tk.E), padx=10)

        # Botones
        ttk.Button(self.frame, text="Agregar Paciente", command=self.agregar_paciente).grid(row=6, column=0, pady=10)
        ttk.Button(self.frame, text="Actualizar Paciente", command=self.actualizar_paciente).grid(row=6, column=1, pady=10)
        ttk.Button(self.frame, text="Eliminar Paciente", command=self.eliminar_paciente).grid(row=7, column=0, pady=10)

        # Tabla (Treeview)
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Nombre", "Edad", "Género", "Historial", "Contacto"),
            show="headings"
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.cargar_paciente_seleccionado)

        self.cargar_pacientes()

    def cargar_pacientes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        pacientes = obtener_pacientes()
        if pacientes:
            for paciente in pacientes:
                self.tree.insert("", tk.END, values=paciente)

    def limpiar_campos(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.edad_var.set("")
        self.genero_var.set("")
        self.historial_var.set("")
        self.contacto_var.set("")

    def cargar_paciente_seleccionado(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, 'values')
            self.id_var.set(values[0])
            self.nombre_var.set(values[1])
            self.edad_var.set(values[2])
            self.genero_var.set(values[3])
            self.historial_var.set(values[4])
            self.contacto_var.set(values[5])

    def agregar_paciente(self):
        try:
            id = self.id_var.get()
            nombre = self.nombre_var.get()
            edad = int(self.edad_var.get())
            genero = self.genero_var.get()
            historial = self.historial_var.get()
            contacto = self.contacto_var.get()

            agregar_pacientes(id, nombre, edad, genero, historial, contacto)
            messagebox.showinfo("Éxito", "Paciente agregado exitosamente.")
            self.limpiar_campos()
            self.cargar_pacientes()
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar paciente: {e}")

    def actualizar_paciente(self):
        try:
            id = self.id_var.get()
            nombre = self.nombre_var.get()
            edad = int(self.edad_var.get())
            genero = self.genero_var.get()
            historial = self.historial_var.get()
            contacto = self.contacto_var.get()

            actualizar_paciente(id, nombre, edad, genero, historial, contacto)
            messagebox.showinfo("Éxito", "Paciente actualizado exitosamente.")
            self.limpiar_campos()
            self.cargar_pacientes()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar paciente: {e}")

    def eliminar_paciente(self):
        try:
            id = self.id_var.get()
            if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este paciente?"):
                eliminar_paciente(id)
                messagebox.showinfo("Éxito", "Paciente eliminado exitosamente.")
                self.limpiar_campos()
                self.cargar_pacientes()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar paciente: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PacientesApp(root)
    root.mainloop()
