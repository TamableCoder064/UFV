# Número aleatorio del 1 al 100 y ver si el numero que pone el usuario coincide,
# si no coincide le pide otra vez constantemente y a la cuarta para

# Sin variable de contador de intentos
import random
numero = random.randint(0,100)
print(numero)
for z in range(4):
    cliente = int(input('Te quedan '+ str(4-z) + ' intento/s, introduce un número:'))
    if cliente == numero:
        print('Has acertado')
        break
    else:
        print('Has fallado')
    print('No te quedan más intentos, el número era ' + str(numero))

# Con variable de contador de intentos
intento = 4
for z in range(intento):
    cliente = int(input('Te quedan '+ str(intento-z) + ' intento/s, introduce un número:'))
    if cliente == numero:
        print('Has acertado')
        break
    else:
        print('Has fallado')
    print('No te quedan más intentos, el número era ' + str(numero))

# Se puede hacer con while
intento = 4
var_control = 0
while var_control < intento:
    cliente = int(input('Te quedan '+ str(intento-var_control) + ' intento/s, introduce un número:'))
    if cliente == numero:
        print('Has acertado')
        break
    else:
        print('Has fallado')
        var_control += 1
if cliente != numero:
    print('No te quedan más intentos, el número era ' + str(numero))