# BUCLES
# En Python solo existe while y for

i = 1
while i < 6:
    print(i)
    i += 1

# Con la construcción break se puede parar un bucle aunque la condición sea verdadera

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1

# Con la instrucción continue se puede parar la iteración del bucle y continuar con la siguiente instrucción
    
i = 1
while i < 6:
    i+=1
    print(i)
    if i == 3:
        continue
    print(i)

# Con la instrucción else se puede ejecutar un bloque de código una vez que la condición sea verdadera

#La variable de control es la que aparece en el while y se usa para salir de un bucle
    
# Puedes asignar una variable con la nada
x = None

# Orden del Script (por convención):
# Imports
# Funciones y clases
# Main
    # variables
    # Logica

# Bucle for permite repetir el bloque un número predeterminado de veces

for i in range(6): #Empieza siempre en el 0, me imprime los valores del 0 al 5
    print(i)

# Se ejecuta tantas veces el bloque de código como elementos tenga el  elemento iterable
    

# Pregunta tipica la del return, en funciones cualquier instrucción que se ponga después del return no se ejecuta nunca.

# Tipos de datos avanzados:
    # Lista (conjunto de datos ordenado de elementos y alterable), 
    # Tupla (es un conjunto de elementos ordenado y no alterable. Permite elementos duplicados)
    # Set (es un conjunto de elementos desordenados e indexado, no permite elementos duplicados)
    # Diccionario (es un conjunto desordenado, cambiable e indexado de elementos. No permite elementos duplicados.)

# LISTAS

list_names = ['Ana', 'Pedro', 'Ramón']
print (list_names)

# Mismo o diferente tipo de variables
list_varios = [1, 'Ana', 4, 'Pepe']

# Pueden tener muchos niveles de anidamiento
list_mult = [['Ana', 'Pedro', 'Ramón'],[1, 'Ana', 4, 'Pepe']]
list_mult_2 = [
    ['Ana', 'Pedro', 'Ramón'],
    [1, 'Ana', 4, 'Pepe']
]

# Para una tupla de un solo elemento
list_elemental = list([2])
list_elemental_2 = [2,]

# Accede a cada elemento a través de un índice numérico
print(list_names [2])  # Contando hacia adelante
print(list_names [-2]) # Contando hacia atrás

# Accede a un rango de índices
print(list_names[2:3])
print(list_names[:3])    # Comenzará en el primer elemento
print(list_names[2:])    # Continuará hasta el final
print(list_names[-4:-1]) # Índices negativos

# El primer índice es el 0, la búsqueda empezará en el primer índice indicado (incluído) y terminará en el último indicado (no incluído)

# Cambiar el valor de los elementos
list_names[2] = 'José'

# Se pueden utilizar como variables de control
for x in list_names:
    print(x)

# Para comprobar la existencia de un elemento
if 'Pedro' in list_names:
    print('Existe')

# Obtener el número de elementos
print(len(list_names))

# Para añadir elementos
list_names.append('Lucas')    # Al final
list_names.insert(2, 'Lucas') # En el lugar indicado

# Para elmiminar elementos
list_names.remove('Ramón') # Un elemento especificado
list_names.pop(2)          # Elimina el índice especificado (sin especificar elimina el último índice)
del list_names[2]          # Elimina el índice especificado (sin especificar elimina toda la lista)
list_names.clear           # Vacía lista

# Copiar una lista
lista2 = list_names          # Copia una referencia, cada cambio se replica
lista2 = list_names.copy()   # Copia sin referenciar, también se puede usar el constructor list()
                             # La diferencia entre estos dos es una pregunta de exámen
lista2 = list_names[:3].copy # Copia solamente los índices especificados

# Unir listas
lista3 = list_names + list_varios
list_names.extend(list_varios)
lista5 = ",".join(list_names)

# Ordenar listas
list_names.sort()    # Orden alfabético
list_names.reverse() # Orden inverso

# TUPLAS

tp_names = ('Ana', 'Pedro', 'Alex')
print(tp_names[0]) # Para acceder a elementos específicos

# Las tuplas funcionan como las listas con la condición de que no son alterables
# Se pueden alterar casteándolas a una lista

list_names = list(tp_names)

# En vez de decir que has hecho una 'ñapa' al cliente se le dice 'Solución de contingencias'

# Para que se considere una tupla hay que ponerle una coma al final para que no lo confunda con un string
tupla = (3,)

# PLEASE GIVE UP