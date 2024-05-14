personajes = {
    'Hitler':['Invadió Polonia','Tiene un bigote precioso','Es alemán','Terminó suicidándose','Exterminó a muchos judíos','Era un gran estratega','Pista 7', 'Pista 8','Pista 9','Pista 10'],
    'Putin':['Invadió Ucrania','Está calvo','Es ruso','Y sabe a fresa','Exterminó a muchos','Es un gran estratega','Pista 7', 'Pista 8','Pista 9','Pista 10'],
    'Patricio':['Invadió mi corazón','Es guapísimo','Mi puto padre','Tiene coche propio','Exterminó a muchos judíos','Era un gran estratega','Pista 7', 'Pista 8','Pista 9','Pista 10']
}
elección = random.choice(list(personajes.keys()))

import random
import time

print('¡Bienvenidos a "ADIVINA EL PERSONAJE"')
print('Tienes un máximo de 10 intentos, con cada intento te daremos una pista')
print('¿Estás preparado?')
usuario = input('Y/N:')
if usuario== 'Y':
    print('Mucha suerte')
else:
    print('Otra vez será')


def ComprobarPersonaje(respuesta):
    if respuesta == elección:
        return True
    return False


