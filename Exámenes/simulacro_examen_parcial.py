# Crear dos funciones, una función llamada ValidarUser que recibirá una cadena con
# el nombre de un usuario, deberá comprobar que el nombre de usuario que recibe cumple las siguientes reglas:

# Tiene un tamaño entre 6 y 12 caracteres.
# No dispone de una coma en el nombre. 
# Está todo en minúsculas.
# Si cumple las tres reglas devolverá True, en caso contrario devolverá False. 

 

# También se debe crear la función llamada ValidarPass que recibirá una contraseña,
# deberá comprobar que la contraseña recibida cumple con los siguiente criterios:

# Tiene al menos 6 caracteres.
# Dispone de al menos un carácter en minúscula, otro en mayúscula y un número. 
# Si cumple las dos reglas devolverá True, en caso contrario devolverá False.

def ValidarUser(nombre_usuario):
    if 6 <= len(nombre_usuario) <= 12 and ',' not in nombre_usuario and nombre_usuario.islower():
        return True
    return False

def ValidarPass(contraseña):
    mayuscula = minuscula = numero = False
    if len(contraseña) >= 6:
        for letra in contraseña:
            if letra.islower():
                minuscula = True
            elif letra.isupper():
                mayuscula = True
            elif letra.isdigit():
                numero = True
        if minuscula and mayuscula and numero:
            return True
    return False

# Crear otra función que se llamará ComprobarUsuarios, que recibirá un diccionario de usuarios (al menos 5). 
# Esta función deberá calcular si el usuario y la contraseña son válidos (ambos), deberá comprobar que recibe
# un diccionario, en caso contrario deberá lanzar una excepción indicando la problemática.
# Si ambos son válidos, deberá añadir al diccionario dentro del usuario la clave "success" con True
# si ambos son válidos o con False si alguno de los dos no lo es. 
# La función devolverá el diccionario resultante. 

# FORMATO DICCIONARIO DE ENTRADA:
# {
#    "pepe": { "password": "pepe1" },
#    "pepe.perez": { "password": "AApggepe1" },
#    "pepe,perez": { "password": "AApggepe1" },
#    "ramon_sanchez": { "password": "rrrrrrrrrr" },
#    "ramon.lopez": { "password": "R4m0N23" }
# }

# FORMATO DICCIONARIO DE SALIDA:
# {
#   'pepe': {'password': 'pepe1', 'success': False},
#   'pepe.perez': {'password': 'AApggepe1', 'success': True},
#   'pepe,perez': {'password': 'AApggepe1', 'success': False},
#   'ramon_sanchez': {'password': 'rrrrrrrrrr', 'success': False},
#   'ramon.lopez': {'password': 'R4m0N23', 'success': True}
# }
diccionario = {
   "pepe": { "password": "pepe1" },
   "pepe.perez": { "password": "AApggepe1" },
   "pepe,perez": { "password": "AApggepe1" },
   "ramon_sanchez": { "password": "rrrrrrrrrr" },
   "ramon.lopez": { "password": "R4m0N23" }
}
def ComprobarUsuario(diccionario):
    if type(diccionario) != dict:
        raise Exception('Esto no es un Diccionario')
    for clave,valores in diccionario.items():
        pwd = valores['password']
        if ValidarUser(clave) and ValidarPass(pwd):
            diccionario[clave]['success'] = True
        else:
            diccionario[clave]['success'] = False
    return print(diccionario)

ComprobarUsuario(diccionario)


# Dado el diccionario resultante del ejercicio 2, deberá contabilizar cuantos usuarios-passwords
# no son válidas y mostrarlo por pantalla con este formato:

# Numero de usuarios: 5
# Válidos: 2
# No válidos: 3

numero_de_usuarios = usuarios_validos = usuarios_no_validos = 0

for k in diccionario.values():
    numero_de_usuarios += 1
    if k['success'] == True:
        usuarios_validos += 1
    else:
        usuarios_no_validos += 1

print(f'Número de usuarios: {numero_de_usuarios}')
print(f'Válidos: {usuarios_validos}')
print(f'No válidos: {usuarios_no_validos}')