# 1. Definir una función que reciba una serie de parámetros indeterminados de tipo clave-valor
#    y un elemento que por defecto será un numero aleatorio.
#    La función deberá comprobar si el número está entre los valores recibidos,
#    si es así mostrará "Existe" y si no mostrará "No Existe".
import random
def Existe(numero=random.randint(1,10), **Elementos):
    if numero in Elementos.values():
        return print('Existe')
    return print('No existe')

# 2. Definir una función que reciba una tupla de notas y calcule la media simple.
#    Para calcular la media simple se debe realizar el sumatorio de cada una de las
#    notas y dividirlo entre en numero total de notas que hay.

def Media(numeros):
    return print(sum(numeros)/len(numeros))

# 3. Definir una función que reciba una lista de números decimales y devuelva esa lista ordenada,
#    no será posible usar la función sort.

def Ordenar(lista_decimal):
    for i in range(1, len(lista_decimal)):
        valor_actual = lista_decimal[i]
        posicion = i
        while posicion > 0 and lista_decimal[posicion - 1] > valor_actual:
            lista_decimal[posicion] = lista_decimal[posicion - 1]
            posicion -= 1
        lista_decimal[posicion] = valor_actual
    return lista_decimal