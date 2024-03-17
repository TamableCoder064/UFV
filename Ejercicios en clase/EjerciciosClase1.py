# De la lista de notas saca la lista de aprobados y suspensos sin alterar el orden

lst_notas = [5,7,9,10,3,6,4,5]

# Solución Oscar
lst_aprobados = list()
lst_suspensos = list()

for x in lst_notas:
    if x >= 5:
        lst_aprobados.append(x)
        lst_suspensos.append('-')
    else:
        lst_suspensos.append(x)
        lst_aprobados.append('-')

for i in range(len(lst_aprobados)):
    if lst_aprobados[i] != '-':
        print(f'El alumno {i+1} ha aprobado con un {lst_aprobados[i]}')
    
for i in range(len(lst_suspensos)):
    if lst_suspensos[i] != '-':
        print(f'El alumno {i+1} ha suspendido con un {lst_suspensos[i]}')

# Solución Dany

for i, nota in enumerate(lst_notas):
    if nota >= 5 in lst_notas: print('El alumno', i+1, 'ha sacado:',nota,'por lo tanto está aprobado')
for i, nota in enumerate(lst_notas):
    if nota < 5 in lst_notas: print('El alumno', i+1, 'ha sacado:',nota,'por lo tanto está aprobado')