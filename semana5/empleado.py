# archivo: empleado.py
from datetime import datetime

class Empleado:
    def __init__(self, nombre, salario, fecha_ingreso):
        self.nombre = nombre
        self.salario = salario
        self.fecha_ingreso = fecha_ingreso

    def calcular_antiguedad(self):
        hoy = datetime.now()
        diferencia = hoy - self.fecha_ingreso
        return diferencia.days // 365

    def obtener_beneficios(self):
        antiguedad = self.calcular_antiguedad()
        beneficios = []
        if antiguedad >= 5:
            beneficios.append("Bono anual")
        if antiguedad >= 3:
            beneficios.append("5 días adicionales de vacaciones")
        return beneficios
