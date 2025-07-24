frutas = ["manzana", "pera", "tuna", "sandía", "plátano"]

print (frutas[0])

#Modificar elemento
frutas[1] = "uva"
print(frutas)

#Agregar elemento
frutas.append("kiwi")
print(frutas)

#Insertar elemento en posición determinada
lista = [1, 2, 3, 4]
lista.insert(3, "holi")

print(lista)

#Elimina un elemento de la lista
lista = [1, 2, 3, 4]
lista.remove(2)

print(lista)

#invertir el orden de la lista
lista = [1, 2, 3, 4]
lista.reverse()

print(lista)

#Elimina un elemento y devuelve el elemento en la posición especificada.
lista = ["seba", "miguel", "eusebio", "miranda"]

elemento_eliminado = lista.pop(1)

print(elemento_eliminado)

