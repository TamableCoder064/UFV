# FUNCIONES Y EXCEPCIONES

# Para nombrar funciones es buena práctica que empiecen con mayúscula
# (las variables recordemos que era buena práctica que empiecen en minúsculas)

# Las funciones son bloques de código que repito y la invoco tantas veces como yo quiera

# Definición de una función
def Func1():
    print('Hello World')

# Llamada a la función func1
Func1()

# Las mayores ventajas de usarlas son las posivilidades de hacer módulos
# Nos permite no repetir código (reutilización)

# Para definir una función
def NOMBRE(LISTA_DE_PARÁMETROS):
    '''DOCSTRING_DE_FUNCIÓN''' #Es una buena práctica para documentar qué hace la función
    # SENTENCIAS (realiza algo)
    # RETURN [EXPRESIÓN] (no es obligatorio, devuelve el valor de la expresión o variable de la función) (Puede devolver más de una con comas)
    pass #Para dejar vacía la función

# Todos los bloques deben estar indentados

# Un parámetro de entrada  son información que se pasa a las funciones, se especifican después del nombre de la función, entre los paréntesis.
# Si son varios parámetros de entrada se deben separar por comas.


def Suma(op1, op2):
    return op1 + op2

print(Suma(4,5))

# ARGUMENTOS DETERMINADOS
# Si no especificamos parámetro de entrada podemos poner uno por defecto (Primero el parámetro obligatorio y luego el opcional)
def Resta(op1, op2=3):
    print(op1-op2)

Resta(8)

# Argumentos indeterminados
def Nombres(*noms):
    for n in noms:
        print(n)

Nombres('Oscar', 'David')
# Con un asterisco te convierte los argumentos los mete en una tupla

# Con dos asteriscos los mete en un diccionario
def Suma(**op):
    print ('El operador 1 tiene el valor:' + str(op['op1']))
    print ('El operador 2 tiene el valor:' + str(op['op2']))
    print ('El operador 3 tiene el valor:' + str(op['op1']+op['op2']))

Suma(op2=5, op1=20)

# Argumentos desordenados
# Se puede llamar a las funciones con los argumentos desordenados siempre que se les especifique la clave y el valor asignado
Resta(op2=8, op1=5)

# Excepciones
# Es un bloque para poder recoger errores y que no se rompa el programa

try:
    print(x)
except:
    print('Excepción x no existe')

# Jerarquía de más específico a menos, y luego siempre el genérico.
# El bloque finally  para realizar una ejecución independientemente de si ha dado o no el error
try:
    print(x)
except NameError:
    print('Excepción x no existe')
except:
    print('Otras excepciones')
finally:
    print('Final')

# Rise sirve para forzar errores que quieres controlar tú
x = -1

if x < 0:
    raise Exception('Error el número es negativo')