# EJERCICIO DE PRUEBA DE LOS APUNTES T5
# Definir un diccionario con las claves [...]
archivo = {
    'Fecha_de_nacimiento': 2003,
    'Nombre': 'Oscar',
    'Apellidos': 'Huelin Mateos',
    'Color_de_pelo': 'Marrón',
    'Color_de_ojos': 'Azul',
    'Peso': 93.5,
    'DNI': '05291049Y',
}
# Cambiar el valor del paso al peso actual más 0,5
archivo['Peso'] += 0.5
print(archivo['Peso'])
# Visualiza todas las claves del diccionario
for claves in archivo:
    print(claves)
# Visualiza todos los valores del diccionario
for valores in archivo:
    print(archivo[valores])
# Visualiza todas las claves y los valores del diccionario con el formato 'Nombre: Pedro'
for claves, valores in archivo.items():
    print(f'{claves}: {valores}')

# EJERCICIO 2
# Definir un diccionario persona1 con las claves [...]
persona1 = {
    'fecha_de_nacimiento': "19 septiembre 2003"
}
# Definir otro diccionario persona2 con las mismas claves que el 1 pero con otros valores
persona2 = {
    'fecha_de_nacimiento': "18 septiembre 2003"
}
# Crear un tercer diccionario que contenga los dos anteriores
personas = {
    'persona1': persona1,
    'persona2': persona2,
}
# Recorre con un bucle while el diccionario personas e imprime los datos
# Solución Danre/Ingrid
i = 0
while i < len(personas):
    print(personas['persona'+str(i+1)])
    i += 1
# Solución Dany
claves = list(personas.keys())
i = 0
while i < len(claves):
    clave = claves[i]
    valor = personas[clave]
    print(f'{clave} {valor}')
    i += 1

# Recorre con un bucle for el diccionario y mostrar solo el nombre y el DNI.
# Además añade 
for key, value in personas.items():
    print(key, value)