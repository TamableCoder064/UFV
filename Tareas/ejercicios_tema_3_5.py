# 1. Definir la función: Division
# 2. Esta función recibirá dos parámetros de entrada el dividendo y el divisor.
# 3. La función debe realiza una división con los dos operadores y devolver el
# resultado.
def Division(dividendo, divisor):
    solucion = dividendo / divisor
    return print(solucion)

# 4. Realizar la siguiente llamada a la función: Division(2,0) y comentar el
# resultado con la clase.
'''Division(2,0)
Nos interrumpe el código con el error [ZeroDivisionError: division by zero]'''

# 5. Añadir un bloque try ... except... controlando el error anterior.
def Division(dividendo, divisor):
    try:
        solucion = dividendo / divisor
        return print(solucion)
    except ZeroDivisionError:
        print('ERROR: No se puede dividir por 0')

# 6. Probar de nuevo la división por 0
Division(2,0)

