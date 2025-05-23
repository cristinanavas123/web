# Cadenas
cadena_simple = "Bienvenido Equipo"
cadena_doble = "La Inteligencia Artificial es lo máximo"

# Concatenación de cadenas
saludo_completo = cadena_simple + " " + cadena_doble

print(saludo_completo)

# Formato de Cadenas

cadena_simple = " Grupo 21 "
cadena_doble = " Te damos la bienvenida a este maravilloso grupo, aquí encontrarás un equipo colaborativo "

# Concatenación de cadenas

bienvenida_completa = cadena_simple + " " + cadena_doble

print(bienvenida_completa)

# Subcadenas y Métodos

cadena_larga = " Hoy en Medellín está lloviendo mucho y hay inundaciones, el tráfico se pone pesado "
lista_de_palabras = cadena_larga. split()

print(lista_de_palabras)

# Métodos de Mayúsculas y Minúsculas

cadena = "Bienvenidos a Manizales"
mayusculas = cadena.upper()
minusculas = mayusculas.lower()

print("original:", cadena)
print("En mayusculas:" , mayusculas)
print("De nuevo en minusculas:" , minusculas)

# Operaciones Aritméticas

a = 10
b = 5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
exponente = a ** b

print("suma:", suma)
print("resta:", resta)
print("multiplicacion", multiplicacion)
print("division" , division)
print("exponente" , exponente)

# Division y Modulo

c = 10
d = 3

resultado = c // d
residuo = c % d

print("resultado:" , resultado)
print("residuo:" , residuo)

# Precisión de Flotantes

c = float(3.14)
entero = 2

suma = c + entero
resta = c - entero
multiplicacion = c * entero
division = c / entero

print("Suma:", suma)
print("resta:", resta)
print("multiplicacion", multiplicacion)
print("division" , division)

# Cömo se manejan las operaciones mixtas En Python, cuando realizas operaciones mixtas entre enteros (int) y decimales (float), el resultado se convierte automáticamente en float para conservar la parte decimal. Este comportamiento se llama "promoción de tipos".