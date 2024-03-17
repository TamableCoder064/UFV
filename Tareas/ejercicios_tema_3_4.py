# 1. Crea un diccionario con 5 parejas clave-valor. Tiene que haber:
#     - Una lista.
#     - Una variable de tipo float.
#     - Una tupla.
#     - Dos variables de tipo texto.
diccionario = dict(lista=[1,2,3], var_float=11.9, tupla=(4,5,6), var_texto1='Hola', var_texto2='Adios')

# 2. Imprime el contenido de la variable de tipo float que has creado dentro del diccionario.
print(diccionario['var_float'])

# 3. Mediante un bucle for, imprime cada uno de los elementos de la lista que has creado dentro del diccionario.
for valor in diccionario['lista']:
    print(valor)

#     Haz lo mismo con un bucle while.
i = 0
while i < len(diccionario['lista']):
    print(diccionario['lista'][i])
    i += 1

# 4. Añade un nuevo elemento a la lista que has creado dentro del diccionario e imprime la lista.
diccionario['lista'].append('Nuevo elemento')
print(diccionario['lista'])

# 5. Modifica el valor de una de las variables de tipo texto que has creado dentro del diccionario e imprime su nuevo valor por pantalla.
diccionario['var_texto2'] = 'Hasta pronto'
print(diccionario['var_texto2'])

# 6. Imprime el último valor de la tupla que has creado dentro del diccionario.
print(diccionario['tupla'][-1])

# 7. Mediante un bucle for imprime todas las parejas clave-valor del diccionario.
#     Ejemplo de la salida esperada de una pareja de clave valor -> La clave 'Apellido1' tiene el valor 'Carreras'.
#     RESPETAD ESTE EJEMPLO.
for k, v in diccionario.items():
    print('La clave ',k,'tiene el valor ',v)

# 8. Añade una nueva pareja clave-valor de tipo entero y elimina completamente la tupla que ya existía en el diccionario.
#     Imprime solo la nueva pareja clave-valor añadida.
diccionario['new_int'] = 22
diccionario.pop('tupla')
for clave, valor in diccionario.items():
    if clave == 'new_int':
        print(clave, valor)

# 9. Crea una copia del diccionario y modifica el valor de 2 parejas clave-valor. Imprime el nuevo diccionario y el original.
diccionario2 = diccionario.copy()
diccionario2['var_texto1'] = 'Muy buenas'
diccionario2['var_texto2'] = 'Que tengas un buen día'
print('\n', diccionario, '\n', diccionario2)

# 10. En el nuevo diccionario, añade dentro de él otro diccionario con al menos 2 parejas clave-valor.
#     Imprime por pantalla el diccionario que tiene otro diccionario dentro, mediante un bucle for.
diccionario2['sub_diccionario'] = dict(nombre='Oscar', apellido='Huelin')
for clave, valor in diccionario2.items():
    if clave == 'sub_diccionario':
        print(clave, valor)