# DICCIONARIOS
# Son colecciones desordenadas, alterables e indexadas de elementos.
# Se delimitan por llaves y contienen pares de clave - valor separados por comas.

nombre_dic = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    # etc.
}

dict1 = {
    'Película': 'Thor',
    'Año': 2011,
    'Director': 'Kerneth Branagh',
    'Segundo_diccionario':{
        'Fila': 5,
        'Asiento': 'B'
    }
}

# Las claves SIEMPRE tienen que ser en formato string
# Los valores pueden ser cualquier tipo

# Se accede a un diccionario a través de las claves
print(dict1['Película'])

# Se puede acceder a un elemento también a través de un métido de la clase dict llamado get()
print(dict1.get('Película'))

# Es alterable, para realizar un cambio de valor se hace a través de su clave
dict1['Película'] = 1.83

# Se puede recorrer con un FOR
# Para que te lo devuelva con las claves
for k in dict1: #se puede añadir al dict1.keys() pero en este caso es redundante
    print(k)

# Para que te devuelva el valor
for k in dict1:
    print(dict1[k])
# También con la función values
for v in dict1.values():
    print(v)

# Puedes acceder a las claves y valores
for k, v in dict1.items():
    print(k,v)

# Al igual que en las listas y las tuplas se puede comprobar la existencia de una clave
if 'Nombre' in dict1:
    print('Existe el Nombre')

# La longitud se puede obtener el tamazo del diccionario (el numero de claves-valor)
print(len(dict1))
# Para acceder a la longitud de otro diccionario dentro de ese diccionario
print(len(dict1['Segundo_diccionario']))

# Para añadir elementos se ha de realizar una asignación de una nueva clave y su valor
dict1['Email'] = 'oscar.huelin@gmail.com'

# Para eliminar elementos

# Elimina con la clave especificada
dict1.pop('Email')

# Elimina el último elemento insertado
dict1.popitem()

# Elimina el elemento con la clave especificada
del dict1['Email']

# Para borrar por completo un diccionario
del dict1     # Método 1
dict1.clear() # Método 2

# Copiar diccionarios
dict2 = dict1
dict2.copy(dict1)

# Anidar diccionarios

# Método 1
dict_anidado = {
    'dict1': {
        'nom': 'Pedro',
        'ape': 'Pérez'
    },
    'dict2': {
        'nom': 'Pedro',
        'ape': 'Pérez'
    }
}

# Método 2

dict1 = {
    'nom': 'Pedro',
    'ape': 'Pérez'   
}

dict2 = {
    'nom': 'Pedro',
    'ape': 'Pérez'   
}

dict_anidado = {
    'dict1': dict1,
    'dict2': dict2
}


# Para crear un diccionario rápido se puede usar el constructor dict()
dict1 = dict(nom='Pedro', ape='Pérez', fecha_nacimiento='01/01/2001')

# fromkeys() devuelve un diccionario con las claves-valor especificadas)
# keys te devuelve una lista con las claves
# setdefault() devuelve el valor de la clave especificada, si no existe la clave, la inserta con el valor indicado
# update() actualiza o inserta el par clave-valor especificado