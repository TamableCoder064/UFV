# HERENCIA

# Es el mecanismo por el cual una clase permite heredar las características (atributos y métodos) de otra clase.
# A la clase de la que se hereda se le llama clase Padre o clase Base.
# A la clase que hereda se le llama clase Hija o clase Derivada/Heredada.

# En python por defecto solo hereda los métodos (no los atributos).

# Clase Padre:
class NombreClasePadre:
    propiedad = 1

# Clase Hija:
class NombreClaseHija(NombreClasePadre):
    # Definición clase hija
    pass

# Cuando se quiere definir una clase, función o método que no haga nada se deberá utilizar la palabra reservada 'pass'

# Si no se define un constructor de la clase hija,
# por defecto llamará al constructor de la clase padre y heredará todo (métodos y atributos)
# En cuanto añadimos un constructor de la clase hija ya no llama al constructor de la clase Padre por defecto y por tanto no vamos a heredar todo (solo los métodos).
# Para heredar todo si sobreescribimos el constructor de la clase hija llamamos a la clase padre con la función super().

class Persona():
    def __init__(self, nom, ape):
        self.nom = nom
        self.ape = ape

class Alumno(Persona):
    def __init__(self, nom, ape):
        super().__init__(nom, ape)

# Herencia Múltiple:
class ClasePadre1():
    pass
class ClasePadre2():
    pass
class NombreClase(ClasePadre1, ClasePadre2):
    pass

# Sobreescribir métodos: se sustituye el comportamiento del método de la clase padre por el de la hija al definir el método con el mismo nombre

# Para determinar si un objeto es una instancia de una clase o no:
isinstance(object, NombreClase)

# Para determinar si una clase es una cubclase
issubclass(NombreClaseHija, NombreClasePadre)

# POLIMORFISMO
# El core de python no permite Overload (dos métodos que reciben diferentes parametros de entrada)
# porque aplica por defecto la sobreescritura

# Clase base
class Vehiculo:
    # Constructor
    def __init__(self):
        self.peso = 0
        self.largo = 0
        self.ancho = 0

    # Métodos
    def GetPeso(self):
        return self.peso
    
    def GetLargo(self):
        return self.largo
    
    def GetAncho(self):
        return self.ancho
    
# Clase derivada
class Coche(Vehiculo):
    # Constructor:
    def __init__(self, peso, largo, ancho, marca, modelo):
        super().__init__()
        # Inicialización datos
        self.SetPeso(peso)
        self.SetLargo(largo)
        self.SetAncho(ancho)
        self.marca = marca
        self.modelo = modelo

    # Métodos:
    def SetPeso(self, peso):
        self.peso = peso
    
    def SetLargo(self, largo):
        self.largo = largo
    
    def SetAncho(self, ancho):
        self.ancho = ancho

    # Sobreescritura:
    def GetPeso(self):
        return (str(self.peso) + ' Kg.')
    
    def GetLargo(self):
        return (str(self.largo) + ' metros')
    
    def GetAncho(self):
        return (str(self.ancho) + ' metros')
    
    def __str__(self) -> str:
        datos = 'Datos del ' + self.marca + ' ' + self.modelo + ':'
        datos += '\n >> Peso: ' + self.GetPeso()
        datos += '\n >> Largo: ' + self.GetLargo()
        datos += '\n >> Ancho: ' + self.GetAncho()
        return datos

# Instanciamos la clase Cahce
car = Coche(1197, 4.2, 1.8, 'Seat', 'Leon')
print(car)

# Sobrecarga (overload): dos metodos con el mismo nombre pero diferentes parámetros de entrada y funcionalidad

# Clase base
class Sobrecarga:
    # Métodos
    def unMetodo(self):
        print('Sobrecarga')
    
    def unMetodo(self, s):
        print(s)

s = 'método sobrecargado'
# Instancia de Sobrecarga
sobre = Sobrecarga()
sobre.unMetodo()
sobre.unMetodo(s)
# En python no es factible (TypeError: unMetodo() missing 1 rquired positional argument:'s')

# Se soluciona con parámetros opcionales:

# Clase base
class Sobrecarga:
    # Métodos
    def unMetodo(self, s = None):
        if s is not None:
            print(s)
        else:
            print('Sobrecarga')

s = 'método sobrecargado'
# Instancia de Sobrecarga
sobre = Sobrecarga()
sobre.unMetodo()
sobre.unMetodo(s)

# Sobreescritura (overriding): dos métodos tienen el mismo nombre, pero pueden tener distinta cabezera y acciones

class Vehiculo(object):
    def __init__ (self):
        self.peso = 0

    def getPeso(self):
        return self.peso

class Coche(Vehiculo):
    def getPeso(self):
        return self.peso + 2500
    
c = Coche()
print(c.getPeso())