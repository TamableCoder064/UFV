print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 1')

if __name__ == "__main__":
# Imprime por pantalla tu nombre y apellidos
    print('Oscar Huelin Mateos')

# Crea una variable de tipo int con tu edad e imprímela por pantalla (Ej: "Mi edad es X años")
    edad = 20
    print('Mi edad es '+ str(edad) + ' años')

# Crea una variable de tipo bool que sea True e imprímela por pantalla.
    argumento = True
    print(argumento)

# Crea dos variables de tipo float con 2 decimales y muestra por pantalla la suma de ambas.
    x = 9.5
    y = 7.3
    print(x+y)

print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 2')

if __name__ == "__main__":
# Crea una variable de tipo tupla, otra de tipo lista, otra de tipo cadena y otra que sea un número
# con los valores que quieras e imprímelos por pantalla siguendo el siguienteorden:
# 1º Número.
# 2º Cadena.
# 3º Lista.
# 4º Tupla.

    var_tupla = ('Bardo','Lux','Pyke')
    var_lista = ['Mordekaiser','Nasus','Urgot']
    var_string = 'Gnar'
    var_int = 6

    print(var_int)
    print(var_string)
    print(var_lista)
    print(var_tupla)

print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 3')

if __name__ == "__main__":
# Realiza una operación de suma, otra de resta, otra de multiplicación y
# otra de división e imprímelos en el siguiente orden:
# 1º Suma.
# 2º Resta.
# 3º Divisón.
# 4º Multiplicación.

    a = 2
    b = 3
    c = 6

    print(a + b)
    print(b - a)
    print(c * a)
    print(c / a)

# EXTRA: Calcula el resto de la división 33 entre 3 e imprímelo por pantalla.
    d = 33
    print(d % b)

print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 4')
if __name__ == "__main__":
# Crea 5 números en una sola línea de código que tengan el valor 4.
    o = p = q = r = s = 4

# Incrementa en 2 el valor del 1º de ellos.
    o += 2

# Decrementa en 1 el valor del 2º de ellos.
    p -= 1

# Multiplica por 3 valor del 3º de ellos.
    q *= 3

# Divide entre 2 valor del 4º de ellos.
    r /= 2

# Calcula el módulo 2 del 5º de ellos.
    s %= 2

# Imprime todos los números resultantes por pantalla.
    print(o)
    print(p)
    print(q)
    print(r)
    print(s)

print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 5')

if __name__ == "__main__":
# Escribe las siguientes condiciones e imprime el mensaje por pantalla en cada caso
# (Recuerda que deberás rellenar las variables y en algún caso, crear tú alguna):

    equipo = 'Real Madrid'
    talla_pie = 47
    ciudad = 'Vva. del Pardillo'

    # Si tu edad es mayor que 18 -> Imprime: "Soy mayor de edad".
    if edad > 18:
        print('Soy mayor de edad')

# Si tu equipo es igual a "Real Madrid" -> Imprime: "Soy madridista".
    if equipo == 'Real Madrid':
        print('Soy madridista')

# Si tu número de zapato es mayor que 45 -> Imprime: "Menudo piezaco!".
    if talla_pie > 45:
        print('Menudo piezaco')
    
# Si tu ciudad es pozuelo -> Imprime: "Soy de Pozuelo".
    if ciudad == 'Pozuelo':
        print('Soy de Pozuelo')

print('--------------------------------------------------------------------------------------------------------------------')
print('EJERCICIO 6')

if __name__ == "__main__":
# Escribe las siguientes condiciones e imprime el mensaje por pantalla en cada caso
# (Recuerda que deberás rellenar las variables y en algún caso, crear tú alguna)
# (Usa el ejercicio anterior como esquema):

# Si tu edad es mayor o igual que 10 -> Imprime: "Soy mayor o igual de 10".
# Si no: Imprime tu edad.
    if edad >= 10:
        print('Soy mayor o igual de 10')
    else:
        print(edad)

# Si tu equipo es igual a "Real Madrid CF" -> Imprime: "Soy madridista".
# Si no: Imprime tu equipo (o si no tienes dilo!).
    if equipo == 'Real Madrid':
        print('Soy madridista')
    else:
        print(equipo)

# Si tu número de zapato es mayor que 44 pero menor que 46 -> Imprime: "Tengo un 45".
# Si no: Imprime tu número de zapato.
    if talla_pie > 44 and talla_pie < 46:
        print('Tengo un 45')
    else:
        print(talla_pie)

# Si tu ciudad es pozuelo o majadahonda -> Imprime: "Vivo cerca de la UFV"
# Si no: Imprime donde vives.
    if ciudad == 'Pozuelo' or ciudad == 'Majadahonda':
        print('Vivo cerca de la UFV')
    else:
        print(ciudad)