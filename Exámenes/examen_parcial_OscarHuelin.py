# Dado el siguiente texto:
texto = '''En un futuro cercano, específicamente en el año 2067, la Tierra se encuentra al borde del colapso ambiental. Con el paso de los años, las cosechas han ido fallando y la atmósfera se ha vuelto cada vez más inhóspita. Cooper, un ex piloto de la NASA, ahora convertido en granjero, es reclutado para una misión especial en el año 2074. La misión consiste en encontrar un nuevo hogar para la humanidad, ya que la Tierra se ha vuelto prácticamente inhabitable.
Cooper se une a un equipo de científicos liderados por el profesor Brand, y entre ellos se encuentra la brillante Amelia Brand. Juntos, emprenden un viaje interestelar a través de un agujero de gusano descubierto cerca de Saturno en el año 2076. Su objetivo es explorar planetas potencialmente habitables en otra galaxia. 
A medida que exploran nuevos mundos, enfrentan peligros desconocidos y desafíos que ponen a prueba su resistencia física y emocional. Descubren que el tiempo en los planetas explorados transcurre de manera diferente al de la Tierra; cada hora allí equivale a años en nuestro planeta. Esta disparidad temporal añade una urgencia desgarradora a la misión, ya que Cooper y su equipo deben luchar contra el tiempo para salvar a la humanidad y reunirse con sus seres queridos.
Con el telón de fondo de un universo vasto e implacable, Interstellar es una épica aventura espacial que explora temas como el amor, el sacrificio, la supervivencia y la búsqueda de nuestro lugar en el cosmos. La película, dirigida magistralmente por Christopher Nolan, fue estrenada en el año 2014 y sigue siendo una obra cinematográfica que desafía la mente y conmueve el corazón de quienes la ven.'''
# Realizar un script que tenga las siguientes acciones: 
# 1. (1 punto) Generar una lista con todos los números existentes en el texto,
# deben estar en formato número y ordenada descendentemente.

# 2. (2,5 puntos) Generar un registro en un diccionario con cada palabra existente
# (independientemente de que esté en mayúscula o en minúscula), excluyendo los números y los símbolos. El diccionario debe tener la siguiente estructura: 

# d = { 
#          "año": {
#                       "veces": 4,  
#                       "donde": [1,4,8,18]
#                    },
#           "Tierra": { ... }
# }
# 3. (1,5 puntos) Generar una tupla con las 5 palabras más repetidas que existan en el texto.
# 4. (0,5 puntos) Mostrar por pantalla los datos de la lista de números con el siguiente formato:
# 1. 345
# 2. 456
# 3. 1996
# ...
# 5. (0,5 puntos) Mostrar las 5 palabras más repetidas que existan en el texto con el siguiente formato:
# Palabra 1 --> en 8 veces.
# Palabra 2 --> un 6 veces. 
# ...


lista_numeros = []
diccionario_palabras = {}
numero_palabra = 0
palabras_mas_repetidas = ()

texto = texto.replace(',', '').replace('.', '')

for palabra in texto.split():
    numero_palabra += 1
    if palabra.isdigit() and palabra not in lista_numeros:
        lista_numeros.append(int(palabra))
    if palabra.lower():
        if palabra not in diccionario_palabras:
            diccionario_palabras[palabra] = {
                      "veces": 1,  
                      "donde": [numero_palabra]
                   }
        else:
            diccionario_palabras[palabra]['veces'] += 1
            diccionario_palabras[palabra]['donde'].append(numero_palabra)


lista_numeros.sort()
lista_numeros.reverse()
print("Lista de números:")
for i, numero in enumerate(lista_numeros, 1):
    print(f"{i}. {numero}")

print(diccionario_palabras)

palabras_ordenadas = sorted(diccionario_palabras.items(), clave=lambda x: x[1]['veces'], reverse=True)[:5]
print("\nPalabras más repetidas:")
for palabra, veces in palabras_ordenadas:
    print(f"{palabra.capitalize()} --> {veces['veces']} veces")