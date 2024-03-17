# 1. Crea una lista con las asiganturas que tienes este cuatrimestre (al menos 3).
if __name__ == "__main__":
    asignaturas = ['Programación', 'Big Data', 'Matemáticas II', 'Orga']

#    Recorre la lista y todas las asignaturas que tengan la letra o, debes eliminarla de la lista.
    for i in asignaturas:
        if 'o' in i or 'ó' in i or 'O' in i:
            asignaturas.remove(i)
#    Muetra las asignaturas resultantes por pantalla por separado. 
    print(asignaturas)

# 2. Crea una lista con 7 numeros.  
if __name__ == "__main__":
    lista_numeros = [2,9,7,1,4,3,5]

#    Haz una copia de la lista, recorre la lista y añade la suma del numero actual 
#    y el anterior a continuación de la posición actual, si es el primer numero se suma contra 0. 
#    Ejemplo: [1,2,3,4,5,6,7,8] 
#    - Cuando estoy en el 1, debe añadir 1 + 0 a la lista --> [1,1,2,3,4,5,6,7,8]
#    - Cuando estoy en el 2, debe añadir 2 + 1 a la lisa --> [1,1,2,3,3,4,5,6,7,8]
    copia_numeros = lista_numeros.copy()
    for elemento in range(len(lista_numeros)):
        if elemento == 0:
            copia_numeros.insert(elemento+1, lista_numeros[elemento])
        else:
            copia_numeros.insert(elemento*2+1, lista_numeros[elemento]+lista_numeros[elemento-1])

# [2,2,9,11,7,16,1,8,4,5,3,7,5,8]

#  Muestra por pantalla la lista resultante. 
    print(lista_numeros)
    print(copia_numeros)
    
# 3. Crea una lista que contenga 5 nombres:
if __name__ == "__main__":
    nombres = ['Dany', 'Diego', 'Patricio', 'David', 'Oscar']

#    - Imprime por pantalla todos los elementos menos el primero y el último. 
    print(nombres[1:-1])
    
#    - Añade la operativa para que borre los 3 últimos.
    del nombres[-3:]

 
# 4. Crea una lista con los numeros del 0 al 10. 
if __name__ == "__main__":
    numeros = list(range(11))
    
# Recorre la lista y genera una nueva lista que en cada posición tenga la lista de 
# la tabla de multiplicar de ese número.  
    nueva_lista = []
    for elemento in numeros:
        tabla = []
        for i in range(11):
            tabla.append(elemento * i)
        nueva_lista.append(tabla)
    print(nueva_lista)