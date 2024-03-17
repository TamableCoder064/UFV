# Ejercicio 1
# Dada una palabra tiene que decirte si es una palabra palindroma
palabra = 'aibofobia'

if list(palabra) == list(reversed(palabra)):
    print('Es palíndroma')
else:
    print('No es palíndromo')

# Se puede hacer con intervalos, el primer parámetro es el inicio, el segundo el final y el tercero de cuánto en cuánto
# Ej. [1:8:2] irá de dos en dos así que para nuestro ejercicio usaremos [::-1]

# Solución de Manuel y Andrés: Con un for realizar esa inversa y comprobar. La diferencia entre recorrer la palabra por índice
# o crear una variable ya revertida es que al ir comprobando letra por letra si no es palíndromo para al detectar la anomalía.
    
r = 1
nombre = 'oso'

for i in range(len(nombre)):
    if nombre[i] == nombre[len(nombre)-r]:
        r += 1
    else:
        break

if r == len(nombre)+1:
    print('Es palíndroma')
else:
    print('No es palíndroma')

# Ejercicio 2
# Imprime los valores de la tupla

x = ['hola', (11,22,32),['oso', 'perro', 'jorge'], 10]

for i in x:
    if type(i) == tuple:
        for z in range(len(i)):
            print(f'Elemento {z+1}: {i[z]}')