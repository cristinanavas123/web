# Creación de tuplas

# Tupla original
mi_tupla = (1, 2, 3, 4, "Anular", "Meñique", "pulgar", "corazón")

# Intentar modificar mi_tupla[8] = "dedo gordo" sale un error TypeError: 'tuple' object does not support item assignment

# Convertir a lista para modificarla
lista_dedos = list(mi_tupla)
lista_dedos[5] = "dedo gordo"  # Modificación

# Convertir de nuevo a tupla si se necesita
mi_tupla_modificada = tuple(lista_dedos)

# Mostrar la tupla modificada
print("Tupla modificada:", mi_tupla_modificada)

# Desempaquetado de tuplas
# Crear la tupla de coordenadas
coordenadas = (19.4326, -99.1332)  # Latitud y Longitud de Ciudad de México

# Desempaquetar la tupla
latitud, longitud = coordenadas

# Mostrar los valores
print("Latitud:", latitud)
print("Longitud:", longitud)

# Operaciones básicas con diccionarios
# Crear el diccionario con tres pares clave-valor
mi_diccionario = {"nombre": "Cristina", "edad": 31, "ciudad": "Medellín"}

# Agregar una nueva clave-valor
mi_diccionario["profesión"] = "Bacterióloga"

# Imprimir solo las claves del diccionario
print("Claves del diccionario:")
for clave in mi_diccionario.keys():
    print(clave)

# Diccionarios Anidados
# Crear el diccionario anidado
contactos = {"persona1": {"nombre": "Santiago","edad": 31, "email": "Santiago@ehotmail.com"}, "persona2": {"nombre": "Juan","edad": 35, "email": "Juan@gmail.com"}}

# Acceder e imprimir información específica de una persona
print("Nombre de persona2:", contactos["persona2"]["nombre"])
print("Edad de persona2:", contactos["persona2"]["edad"])
print("Email de persona2:", contactos["persona2"]["email"])

# Iteración y Actualización

for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave} - Valor: {valor}")

# Actualice el valor de una clave en mi_diccionario.
mi_diccionario["edad"] = 50
print(mi_diccionario)

# Operaciones básicas
# Crear la lista vacía
mi_lista = []

# Agregar los números del 1 al 5 a mi_lista
for i in range(1, 6):
    mi_lista.append(i)

# Imprimir mi_lista
print("Lista antes de eliminar el 3:", mi_lista)

# Eliminar el número 3 de la lista
mi_lista.remove(3)

# Imprimir mi_lista después de eliminar el 3
print("Lista después de eliminar el 3:", mi_lista)

# Rebanado de listas
# Crear la lista de números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Imprimir los primeros tres elementos
print("Primeros tres elementos:", numeros[:3])

# Imprimir los elementos desde el tercero hasta el sexto
print("Elementos desde el tercero hasta el sexto:", numeros[2:6])

# Imprimir los últimos dos elementos
print("Últimos dos elementos:", numeros[-2:])

# Listas y Ciclos
# Tupla original
mi_tupla = (1, 2, 3, 4, "Anular", "Meñique", "pulgar", "corazón")

# Usar un bucle para imprimir cada elemento
for elemento in mi_tupla:
