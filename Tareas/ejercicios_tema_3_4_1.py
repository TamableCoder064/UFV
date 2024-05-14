# Objetivo: 
# Poner en juego los conocimiento adquiridos para crear una aplicación que permita jugar al numero más alto.

# La aplicación debe cumplir las siguientes reglas:
# Deberá interactuar con el usuario para sacar una carta aleatoria para el jugador y una para la computadora. 
# El juego tendrá 5 rondas, deberá informar al usuario de la ronda en la que está y de como va la puntuación. 
# Al finalizar las 5 rondas se deberá mostrar el resultado al usuario y ofrecerle jugar de nuevo o salir en cualquier caso. 
# El orden de las cartas de menor a mayor es: (siendo esta la más baja) 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12, 1 (siendo esta la más alta)
# Se deben guardar los datos de cada ronda en un diccionario con la siguiente estructura: 
# { 
#   "Ronda 1": {
#                       "Jugador": ["Carta 5", 2]
#                       "Computadora": ["Carta 2", 0]
#                     },
#   "Ronda 2": {
#                       "Jugador": ["Carta 3", 2]
#                       "Computadora": ["Carta 12", 2]
#                     },
#     ...
# } 

# La dinámica del juego para cada ronda será:
# El jugador saca carta aleatoria y la computadora también.
# El jugador que tenga la carta más alta ganará 2 puntos. En caso de mismo valor de la carta ambos recibirán 1 punto. El jugador que saque la carta más pequeña se llevará 0 puntos. Estos datos se guardarán en el diccionario. 
# Deberá mostrar la ronda y la puntuación del usuario y la computadora.

# Información adicional:
# Para algunas funcionalidades será necesario utilizar librerías adicionales como random (randint).
# Se permite el uso de input para la interacción con el usuario.

import random
import time

registro_datos = {}
rondas = tuple(range(1,6))
baraja = (1,12,11,10,9,8,7,6,5,4,3,2)
jugador = int()
maquina = int()

print('¡Bienvenido al juego "Carta Alta"!')
time.sleep(1)
print('Donde compites 5 rondas contra la máquina por ver quién saca la carta con el valor más alto')
time.sleep(4)
print('Los valores van del 1 al 12. Siendo el 1 el valor más alto y el 2 el valor más bajo')
time.sleep(3)
print('Por cada ronda que ganes obtienes 2 puntos, 1 en caso de empate y 0 si pierdes')
time.sleep(3)
usuario = input('¿Estás listo? (y/n):')
while usuario.lower() != 'y' and usuario.lower() != 'n':
    print('Perdona, no he entendido lo que me has dicho...')
    usuario = input('¿Estás listo? (y/n):')
if usuario.lower() == 'y':
    print('¡QUE COMIENCE EL JUEGO!')
    for ronda in rondas:
        print(f'Estás en la ronda {ronda}')
        input('Presiona Enter para sacar una carta...')
        
        carta_jugador = random.choice(baraja)
        carta_maquina = random.choice(baraja)

        print(f'Tu carta es: {carta_jugador}')
        time.sleep(1)
        print(f'Carta de la computadora es: {carta_maquina}')
        time.sleep(3)
        
        if carta_jugador > carta_maquina:
            print('¡Has ganado esta ronda!')
            registro_datos[f'Ronda {ronda}'] = {"Jugador": [f"Carta {carta_jugador}", 2], "Computadora": [f"Carta {carta_maquina}", 0]}
        elif carta_jugador < carta_maquina:
            print('La computadora ha ganado esta ronda.')
            registro_datos[f'Ronda {ronda}'] = {"Jugador": [f"Carta {carta_jugador}", 0], "Computadora": [f"Carta {carta_maquina}", 2]}
        else:
            print('Ha sido un empate en esta ronda.')
            registro_datos[f'Ronda {ronda}'] = {"Jugador": [f"Carta {carta_jugador}", 1], "Computadora": [f"Carta {carta_maquina}", 1]}
        
        time.sleep(1)
        print(f'Puntuación actual - Jugador: {registro_datos[f"Ronda {ronda}"]["Jugador"][1]}, Computadora: {registro_datos[f"Ronda {ronda}"]["Computadora"][1]}')
        print()
else:
    print('Ohh... vaya')
    time.sleep(1)
    print('Vuelve cuando estés listo')
    
print('--- Resultados finales ---')
print(registro_datos)

respuesta = input('¿Quieres jugar de nuevo? (y/n): ')
if respuesta.lower() == 'y':
    print('¡Que comience otra partida!')
    registro_datos = {}
else:
    print('Gracias por jugar. ¡Hasta luego!')
