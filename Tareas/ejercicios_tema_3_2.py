print('-'*100)
print('EJERCICIO 1')

# 1. Crea una lista con las asiganturas que tienes este cuatrimestre (al menos 3).
if __name__ == "__main__":

#    Muestra por pantalla las asignaturas que están en índices pares.
    lst_asignaturas = ['Competencias de la transformación digital', 'Matemáticas II', 'Programación II', 'Big Data', 'Organización de empresas II']
    for i in range(len(lst_asignaturas)):
        if i % 2 == 0:
            print(lst_asignaturas[i])

#	 Muestra todas las asignaturas menos la primera. 
    print(lst_asignaturas[1:len(lst_asignaturas)])

print('-'*100)
print('EJERCICIO 2')

# 2. Crea una tupla con al menos 5 elementos. 
if __name__ == "__main__":
    tpl_marcador = ('Kills', 'Deaths', 'Assists', 'KDA')

# 	 Muestra por pantalla el tamaño de la tupla.
    print(len(tpl_marcador))

#	 Muestra por pantalla cada uno de los valores de la tupla. 
    print(*tpl_marcador)

print('-'*100)
print('EJERCICIO 3')

# 3. Crea una lista que contenga:
#    - Una tupla de nombres (al menos 3).
#    - Una lista de notas (al menos 3).
#    - 1 entero.
#    - Dos cadenas de texto.
if __name__ == "__main__":
    lst_general = [('Dany', 'Diego', 'Patricio'), [9,10,8],100,'Barandilla', 'Tómbola']
#	 Imprime por pantalla los elementos de la tupla y de la lista por separado y con el siguiente formato para la tupla:
#     "Elemento numero 1: Pedro"
#     "Elemento numero 2: Paco"
    superindice = 0
    for sub_lista in lst_general:

        if type(sub_lista) == tuple:
            indice = 1
            for valor in sub_lista:
                print(f'Elemento numero {indice}: {valor}')
                indice += 1
#    Para la lista deberá mostrar:
#      "Nota del alumno 0: 5.5"
#      "Nota del alumno 1: 10.0"
        elif type(sub_lista) == list:
            indice = 0
            for valor in sub_lista:
                print(f'Nota del alumno {indice}: {valor}')
                indice =+ 1
#    Ademas debe mostrar un texto indicando de que es cada tipo de la lista original, aunque no muestre su valor.
        print('El elemento ', superindice, 'es un ', type(sub_lista))
        superindice += 1

print('-'*100)
print('EJERCICIO 4')


# 4. Crea una lista con equipos deportivos (al menos 5).
if __name__ == "__main__":
    equipos_deportivos = ['Real Madrid','Atleti','Barcelona','Valencia','Sevilla']
    var_control = 0
#	 Imprime el contenido de la lista con los distintos tipos de bucles que hemos visto (cada juego en una línea).
    for equipo in equipos_deportivos:
        print(equipo, end=' ')
    print()
    while var_control < len(equipos_deportivos):
        print( equipos_deportivos[var_control], end = ' ')
        var_control += 1

print()
print('-'*100)
print('EJERCICIO 5')

# 5. Crea un bucle for que vaya desde 3 a 43 y que imprima si el numero es divisible entre 2 o si lo es entre 7, 
# en caso contrario indicará que no es divisible entre 2 ni 7. 
if __name__ == "__main__":
    for x in range(3,44):
        if x % 2 == 0:
            print(x,' es divisible entre 2')
        elif x % 7 == 0:
            print(x,' s divisible entre 7')
        else:
            print(x,' no es divisible entre 2 ni 7')

print('-'*100)
print('EJERCICIO 5')

# 6. Crea una variable de tipo cadena con el texto 
#    "El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015. 
#	 La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016. 
#    La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017. 
#	 En diciembre de 2017 se renovó la cuarta y última temporada de la serie,​ que fue estrenada el 6 de octubre de 2019."
#	 
#	 Muestra por pantalla cuantos números aparecen en el texto. 
#	 Muestra por pantalla cuantas oes aparecen en el texto.
#    Muestra por pantalla el numero total de letras que hay en el texto. 
if __name__ == "__main__":
    noticiero = '''El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015. 
La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016. 
La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017. 
En diciembre de 2017 se renovó la cuarta y última temporada de la serie, que fue estrenada el 6 de octubre de 2019.'''

    numeros = 0
    oes = 0
    letras = 0

    for caracter in noticiero:
        if caracter.isdigit():
            numeros += 1
        if caracter.lower() == 'o' or caracter.lower() == 'ó':
            oes += 1
        if caracter.isalpha():
            letras += 1
    print(f'El texto tiene {numeros} números, {letras} letras y {oes} oes')