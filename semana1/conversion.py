# Conversión de lista a diccionario

def lista_a_diccionario(lista):

    diccionario = dict(lista)

    return diccionario



# Conversión de diccionario a lista de tuplas



def diccionario_a_lista(diccionario):

    lista = list(diccionario.items())

    return lista



# Conversión de cadena a lista

def cadena_a_lista(cadena):

    lista = cadena.split()

    return lista



# Conversión de lista a cadena

def lista_a_cadena(lista):

    cadena = ' '.join(lista)

    return cadena



# Ejemplos de uso

lista_ejemplo = [('a', 1), ('b', 2), ('c', 3)]

diccionario_ejemplo = {'x': 10, 'y': 20, 'z': 30}

cadena_ejemplo = "Hola, esta es una cadena de ejemplo"

lista_ejemplo_2 = ['Esto', 'es', 'otra', 'lista']



print("Conversión de lista a diccionario:", lista_a_diccionario(lista_ejemplo))

print("Conversión de diccionario a lista de tuplas:", diccionario_a_lista(diccionario_ejemplo))

print("Conversión de cadena a lista:", cadena_a_lista(cadena_ejemplo))

print("Conversión de lista a cadena:", lista_a_cadena(lista_ejemplo_2))