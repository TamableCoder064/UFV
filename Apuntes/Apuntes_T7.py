# TEMA 4
# Paradigma Orientado a Objetos
# Es un diseño de software que nos permite representar objetos de la vida real
# Sirve para separar componentes de un programa

# Dos partes: los datos (Parte NO visible) y la forma en la que nos relacionamos (Parte visible)
#   Los objetos tienen un núcleo que son los datos que almacenamos en ese objeto
#   La capa exterior son las funciones (métodos) de ese objeto

# Atributos es la parte de información que definen al objeto
# Los eventos es cuando llamo a una función de un objeto
# La clase es la plantilla, a raiz de esa plantilla creas objetos
# Un objeto es la instancia de una clase
# Instanciar es definir un objeto

# Abstraccion: Dependiendo del contexto de tu clase vas a enseñar más o menos información de tu clase

# Encapsulación: Cierra los atributos del nucleo lo suficiente para que se interactue con el nucleo a traves de los métodos (clases)
#                Una clase no puede depender de un factor externo

# Polimorfismo: permite a distintos objetos responder de manera diferente a un mismo llamado de método
#   Sobrecarga (overload): Dos metodos con el mismo nombre pero distintos parametros
#   Sobreescritura (overriding): En la herencia se puede sobreescribir en la clase hija
# Python no implementa Sobrecarga

# Herencia: Nos sirve para generar una gerarquía de clases sin repetir atributos y métodos comunes
# Modularidad: Segmentar el código y reutilizarlo tantas veces como necesitamos
# Recolección de basura: Es importante que se vayan quitando los objetos que no se usan
# Refactorizar: Que no haya trozos de código duplicados

# Cómo hacemos una clase:
class NombreClase:
    propiedad = 1

# La clase define tipos de objetos (ej, la clase mesa crea objetos mesa)

# Buena práctica, los atributos de la clase se debería definir (inicializar) en el constructor de la clase

# Cómo instanciamos un objeto:
obj = NombreClase() # Con esto creamos un objeto que pertenece a la clase NombreClase con la propiedad 1 como parte de su núcleo
print(type(obj))    # El tipo de un objeto es el nombre de la clase

# Ejemplo:
class Saludo: # Define la clase
    texto = "Hola" # Crea un atributo y le pone el valor fijo de texto (string)
    # Un método con parámetros (1 parámetro "name", self no se considera un parámetro)
    def saludar(self, name): #self es la referencia interna a la clase, es necesario ponerlo en todos los metodos y atributos de la clase
        print(self.texto + " " + name + "!!!!") # Imprime " [name]!!!!"

p1 = Saludo() # Crea una variable tipo Saludo() que es un texto con Hola
p1.saludar("Oscar") # Utiliza la función saludar en la variable p1

# Existe un método reservado llamado __init__ que es el constructor de la clase
# Será el método al que se llame cuando se instancie un objeto de esa clase
# Se utiliza para 'Iniciar' los atributos del objeto
# El destructor se omite en python con el Garbage Colector

class Saludo:
    def __init__(self, texto): # Definir un parámetro de entrada en el constructor de una clase lo hace "obligatorio"
        self.texto = texto # Le asignamos el valor de la variable texto al atributo self.texto
    def saludar(self, name):
        print(self.texto + " " + name + "!!!!")

p1 = Saludo("Hola")
p1.saludar("Clase")

# Constructor vacío
class Vacío():
    def __init__(self):
        pass
# Pongas o no pongas el constructor vacío python ya lo hace solo
# Si no se va a aportar nada más se considera redundante

# Definir un método:
class NombreClase:
    def miFuncion(self):
        print('Hola Mundo!!!')
# self solo se usa dentro de la clase

# Para acceder a un atributo:
# objeto.nombreatributo('va a tener un valor puede ser lo que queramos; numero, texto, tupla...')

# Acceder a un atributo:
class Saludo:
    
    def __init__(self, nombre):
        self.texto = 'Hola'
        self.nombre = nombre
    
    def saludar(self):
        print('Método -> ' + self.texto + ' ' + self.nombre)

p1 = Saludo('clase')
p1.saludar()
print('Atributos -> ' + p1.texto + ' ' + p1.nombre)

# Para acceder a un método:
# objeto.nombremetodo(parametro1, parametro2, parametro3... si los tuviese)

# Self es la referencia interna al objeto y es OBLIGATORIO ponerlo aunque en la llamada se omite,
# solo se tiene que poner al definir la clase,
# no tiene por que ser 'self', puede ser la palabra que queramos. El estandar en python es self.
class Saludo:
    def __init__(mio, nombre):
        mio.texto = 'Hola'
        mio.nombre = nombre

    def saludar(mio):
        print(mio.texto)

p1 = Saludo('clase')
p1.saludar()

# Modificar una propiedad:
class Saludo:
    def __init__(self, nombre) -> None:
        self.texto = 'Hola'
        self.nombre = nombre

    def saludar(self):
        print(self.texto + ' ' + self.nombre)

p1 = Saludo('clase')
p1.nombre = 'Esteban'
p1.saludar()

# Borrar una propiedad:
class Saludo:
    def __init__(self, nombre) -> None:
        self.texto = 'Hola'
        self.nombre = nombre

    def saludar(self):
        print(self.texto + ' ' + self.nombre)

p1 = Saludo('clase')
print(dir(p1))
del p1.texto
print(dir(p1))

# Borrar el objeto entero:
class Saludo:
    def __init__(self, nombre) -> None:
        self.texto = 'Hola'
        self.nombre = nombre

    def saludar(self):
        print(self.texto + ' ' + self.nombre)

p1 = Saludo('clase')
p1.saludar()
del p1
p1.saludar()

#Llamar a una función:
class Saludo:
    def __init__(self, nombre) -> None:
        self.texto = 'Hola'
        self.nombre = nombre

    def saludar(self):
        print(self.texto + ' ' + self.nombre)

    def despedirse(self):
        print('Adios ' + self.nombre)

p1 = Saludo('clase')
p1.saludar()
p1.despedirse()

# Atributo o métodos privados: añadir dos guiones bajos (__) al inicio para denegar el acceso a los datos.
# Cualquier intento de acceder desde el exterior provocará AttributeError.