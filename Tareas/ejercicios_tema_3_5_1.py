#1. Crea una función que reciba como parámetros 2 números y devuelva si son múltiplos.
def Multiplos(num1,num2):
    if num1%num2 == 0:
        return print(f'El número {num2} es múltiplo de {num1}')
    elif num2%num1 == 0:
        return print(f'El número {num1} es múltiplo de {num2}')
    return print('Ninguno es múltiplo del otro')

#2. Crea una función que reciba una lista y una variable,
#   debe indicar si el elemento que hay en la variable está en la lista y en que posición. 
def ElementoEnLista(lista,elemento):
    if elemento in lista:
        return print(f'"{elemento}" está en la lista en la posición {lista.index(elemento)+1}')
    return print(f'"{elemento}" NO está en la lista')

#3. Crea una función que admita un numero indeterminado de numeros,
#   deberá calcular la media de los numeros (el total de números divididos entre el numero total de números).
def Media(*numeros):
    return print(sum(numeros)/len(numeros))

#4. Crea una función que reciba un texto,
#   deberá devolver ese mismo texto pero con dos espacios adicionales tras cada letra.
def Espacios(texto):
    texto_espaciado=''
    for elemento in texto:
        if elemento.isalpha():
            texto_espaciado += elemento+'  '
        else:
            texto_espaciado += elemento
    return print(texto_espaciado)

Espacios('Hol12346aaaaa')

#5. Crea una función que reciba una lista de números como parámetro y un valor booleano que por defecto será True. 
#   Deberá devolver el máximo valor de todos los números de la lista si el booleano es True,
#   y el mínimo si el valor booleano es False.

# Dos maneras de hacerlo
# Método Oscar:
def MaximoMinimo(lista,booleano=True):
    lista.sort()
    if booleano:
        return print(lista[-1])
    return print(lista[0])

# Método Dany:
def MaximoMinimo(lista,booleano=True):
    if booleano:
        return print(max(lista))
    return print(min(lista))