varNota = int(input("Ingrese la nota del estudiante (0-100): "))

if varNota >= 60 and varNota <= 100:
    print("El estudiante ha aprobado con una nota de:", varNota)

else:
    print("El estudiante ha reprobado con una nota de:", varNota)