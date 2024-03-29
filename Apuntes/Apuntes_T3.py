# Esto es un comentario, no se ejecuta
'''Esto también es un comentario
    en diferentes líneas'''

# Para declarar una variable nombramos y reserva ese espacio en memoria (solo puede empezar por _ o letra)
# CamelCase nombrePrueba, SnakeCase NombrePrueba, otro nombre_prueba

nombreAlumno = 'Oscar Huelin'
print(nombreAlumno)

# Para saber el tipo de variable
x = 'Hola'
print(type(x))

# Asignación múltiple
y,z= 2,3
print (y)
print (z)

# Mismo valor a diferentes variables
# Para escapar el salto de línea por defecto en print agregamos end='' y se agregará en todas y para agregar el salto de línea '\n'
a=b='mismo valor'
print (a, end=' ')
print (b)

print (a+' '+b)

print (a,'',b)

# No se puede concatenar variables de diferentes tipos, hay que castear
# En este caso es un casting explícito
print('El valor de y es '+ str(y) )

# TIPOS DE DATOS
# Text: str  |  Numeric: int, float, complex  | Sequence: list, tuple, range  |  Mapping: dict
# Set: set, frozenset  | Boolean: bool | Binary: bytes, bytearray, memoryview

x = 'Hola Mundo!' #str | son cadenas de caracteres entre comillas simples o dobles
x = '''Las tres comillas se utilizan
        para poder escribir
        en diferentes líneas'''
x = 10                             #int | son números enteros positivos o negarivos
x = 9.5                            #float
x = 1j                             #complex
x = ['Madrid','Sevilla','Toledo']  #list
x = ('Madrid','Sevilla','Toledo')  #tuple
x = range(5)                       #range
x = {'Apel': 'García', 'Edad' :26} #dict
x = {'MAD', 'SEV', 'TOL'}          #set
x = True                           #bool | representan valores True o False
x = b'hello'                       #bytes
x = bytearray(5)                   #bytearray

# Casting es una conversión de variable a un tipo de dato
int() # Conversión a entero

# Los operadores se utilizan para realizar operaciones en variables y valores

# Operadores Aritméticos
x + y # Suma +
x - y # Resta -
x * y # Multiplicación *
x / y # División /
x % y # Módulo (resto) %

# Operadores de Asignación
x = 1  # Asignación x=1
x += 1 # Adición x=x+1
x -= 1 # Resta x=x-1
x *= 2 # Multiplicación x=x*2
x /= 2 # División x=x/2
x %= 2 # Módulo x=x%2

# Operadores de Comparación
x == y # Igual
x != y # Distinto
x > 5  # Mayor que
x < 2  # Menor que
x >= 2 # Mayor o igual que
x <= 2 # Menor o igual que

# Operadores Lógicos
x < 5 and x < 10       # Y
x < 4 or x < 6         # O
not (x == 5 or x == 6) # Invierte el resultado si es verdadero

# Estructuras de control: if (condicional), while (bucle), for (un número determinado de veces)
# Condicionales

n=1
p=7

if n < p:
    print('Menor')
elif n > p:
    print('Mayor')
else:
    print('Igual')

