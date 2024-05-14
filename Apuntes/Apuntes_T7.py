# TEMA 4
# Paradigma Orientado a Objetos
# Es un diseño de software que nos permite representar objetos de la vida real
# Dos partes: los datos y la forma en la que nos relacionamos
# Los objetos tienen un núcleo que son los datos que almacenamos en ese objeto
# La capa exterior son las funciones (métodos) de ese objeto
# Sirve para separar componentes de un programa
# Atributos es la parte de información que definen al objeto
# Los eventos es cuando llamo a una función de un objeto
# La clase es la plantilla, a raiz de esa plantilla creas objetos
# Un objeto es la instancia de una clase
# Instanciar es definir un objeto
# Abstraccion: Dependiendo del contexto de tu clase vas a enseñar más o menos información de tu clase
# Encapsulación: Cierra los atributos del nucleo lo suficiente para que se interactue con el nucleo a traves de los métodos (clases)
# REGLA ENCAPSULACIÓN: Una clase no puede depender de un factor externo
# Polimorfismo: permite a distintos objetos responder de manera diferente a un mismo llamado de método
#   Sobrecarga (overload): Dos metodos con el mismo nombre pero distintos parametros
#   Sobreescritura (overriding): En la herencia se puede sobreescribir
# Herencia: Nos sirve para generar una gerarquía de clases sin repetir atributos comunes
# Modularidad: Segmentar el código y reutilizarlo tantas veces como necesitamos
# Recolección de basura: Es importante que se vayan quitando los objetos que no se usan
# Refactorizar: Que no haya trozos de código duplicados
# Todo en python es una clase (incluídos los str, bool, int...)

# Cómo hacemos una clase:
class NombreClase:
    propiedad = 1

# La clase define tipos de objetos (ej, la clase mesa crea objetos mesa)

# Buena práctica, los atributos de la clase se debería definir en el constructor de la clase

# Cómo instanciamos un objeto:
obj = NombreClase() # Con esto creamos un objeto que pertenece a la clase NombreClase con la propiedad 1
print(type(obj))

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

class Saludo:
    def __init__(self, texto):
        self.texto = texto
    def saludar(self, name):
        print(self.texto + " " + name + "!!!!")

p1 = Saludo("Hola")
p1.saludar("Clase")

