#Escribe esta linea de código:
print ("bienvenidos al entrenamiento python, vamos a disfrutar al máximo esta sesión")

"""
    Descuento en una compra:
    Si compras más de $1000, obtienes un descuento del 20%
    Pide el monto de la compra y muestra el precio final
"""

# Pedir datos por teclado al usuario int (entero) float (decimales) str (cadenas de caracteres) bool (boleanos unos o ceros)

compra = float(input("Por favor digite el valor de la compra: "))

# Si compras más de $1000, obtienes un descuento del 20%
# Siempre que la salida tenfa más de un camino de resolución, debo implementar condicionales

# operadores combinados
# operadores de asignación =, operadores aritméticos + - * /, operadores lógicos and y, or o, not,
# operadores de comparación ==, !=, >, <, >=, <=

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra-descuento # operador de asignación
    compra -= descuento # operador de asignación compuesto
    print (f"El descuesto es de {descuento}, por lo tanto su valor a pagar es: {compra}")


