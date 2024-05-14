# 1. Crea una clase llamada CalculadoraAreas cuyo objetivo es el de calcular
# el área de las siguientes figuras geométricas:
#   - Cuadrado
#   - Rectángulo
#   - Triángulo
#   - Pentágono
#   - Hexágono
#   - Circunferencia
# Cada área se calculará en un método diferente. Los parámetros de entrada
# serán los datos necesarios para el cálculo del área.
# No te olvides del constructor.
# Haz una prueba de cada método.

class CalculadoraAreas:
    def __init__(self):
        pass

    def area_cuadrado(self, lado):
        return lado ** 2

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_triangulo(self, base, altura):
        return 0.5 * base * altura

    def area_pentagono(self, lado, apotema):
        return 5 * lado * apotema / 2

    def area_hexagono(self, lado):
        return 3 * (3 ** 0.5) * lado ** 2 / 2

    def area_circunferencia(self, radio):
        import math
        return math.pi * radio ** 2

calculadora = CalculadoraAreas()
print("Área del cuadrado:", calculadora.area_cuadrado(5))
print("Área del rectángulo:", calculadora.area_rectangulo(4, 6))
print("Área del triángulo:", calculadora.area_triangulo(3, 8))
print("Área del pentágono:", calculadora.area_pentagono(7, 4))
print("Área del hexágono:", calculadora.area_hexagono(5))
print("Área de la circunferencia:", calculadora.area_circunferencia(2))

# 2. Crea una clase en python llamada TextChanger cuyo objetivo es
# contener varios métodos para manipular cadenas de texto. 
# Los métodos que tiene son:
#   - Vuelta: dada una cadena, la función devuelve la misma cadena pero dada la vuelta.
#       EJ: cadena -> anedac
#   - Cambiar: Dada una cadena y 1 letra, la función devuelve la misma cadena pero
#       cambiando todas las veces que aparece la letra por una A.
#   - Eliminar: Dada una cadena, la función devuelve la misma cadena pero sin comas ni puntos.
# No te olvides del constructor.
# Haz una prueba de cada método.

class TextChanger:
    def __init__(self, cadena):
        self.cadena = cadena

    def vuelta(self):
        return self.cadena[::-1]

    def cambiar(self, letra):
        return self.cadena.replace(letra, 'A')

    def eliminar_comas_puntos(self):
        return self.cadena.replace(',', '').replace('.', '')

texto = "Hola, mundo. Esta es una prueba."
tc = TextChanger(texto)
print("Cadena original:", texto)
print("Cadena invertida:", tc.vuelta())
print("Cadena modificada (reemplazar 'o' por 'A'):", tc.cambiar('o'))
print("Cadena sin comas ni puntos:", tc.eliminar_comas_puntos())

# 3. Haz una clase en python que se llame ControladorLista.
# Esta clase tiene un constructor que recibe una lista la cual usa para
# inicializar el atributo de clase Lista.
# La función tiene las siguientes funciones:
#   Anyadir: recibe una variable como parámetro y sirve para añadir un elemento al final de la lista.
#   Anyadir: recibe 2 variables como parámetro y sirve para añadir un elemento en una posición concreta.
#   Eliminar: recibe una variable como parámetro y sirve para eliminar el valor de la lista (si es que está en la lista).

class ControladorLista:
    def __init__(self, lista):
        self.Lista = lista

    def Anyadir(self, elemento, posicion=None):
        if posicion is None:
            self.Lista.append(elemento)
        else:
            self.Lista.insert(posicion, elemento)

    def Eliminar(self, elemento):
        if elemento in self.Lista:
            self.Lista.remove(elemento)
        else:
            print(f"{elemento} no está en la lista.")

mi_lista = [1, 2, 3]
controlador = ControladorLista(mi_lista)
controlador.Anyadir(4)  # Añade 4 al final de la lista
controlador.Anyadir(10, 1)  # Añade 10 en la posición 1
controlador.Eliminar(2)  # Elimina el valor 2 de la lista
print(controlador.Lista)  # Debería mostrar [1, 10, 3, 4]

# 4. Haz una clase en python que se llame Domicilio.
# Esta clase tiene un constructor que recibe los siguientes datos:
#   - TipoVia (calle, plaza, avenida, etc.)
#   - NombreCalle
#   - Numero
#   - Puerta
#   - Piso
#   - CP
#   - Ciudad
#   - Provincia
#   Se deben implmentar métodos para cambiar cualquiera de estos datos.
#   Además se debe implementar un método que muestre la dirección postal completa con el siguiente formato:
#       TipoVia NombreCalle, Numero, Puerta, Piso
#       CP Cuidad
#       Provincia

class Domicilio:
    def __init__(self, TipoVia, NombreCalle, Numero, Puerta, Piso, CP, Ciudad, Provincia):
        self.TipoVia = TipoVia
        self.NombreCalle = NombreCalle
        self.Numero = Numero
        self.Puerta = Puerta
        self.Piso = Piso
        self.CP = CP
        self.Ciudad = Ciudad
        self.Provincia = Provincia

    def mostrar_direccion(self):
        direccion_completa = f"{self.TipoVia} {self.NombreCalle}, {self.Numero}, {self.Puerta}, {self.Piso}\n" \
                             f"{self.CP} {self.Ciudad}\n" \
                             f"{self.Provincia}"
        print(direccion_completa)

mi_domicilio = Domicilio(TipoVia="Avenida", NombreCalle="Principal", Numero="123", Puerta="A",
                         Piso="2", CP="28001", Ciudad="Madrid", Provincia="Comunidad de Madrid")
mi_domicilio.mostrar_direccion()

# 5. Haz una clase en python que se llame DomiciliosPersona.
# Esta clase tiene un constructor que recibirá los datos de la persona:
#   - Lista de objetos tipo Domicilio (ejercicio 4) --> vacía inicialmente
#   - NombrePersona
#   - DNIPersona
#   Se deben implementar los siguiente métodos:
#   AnyadirDomicilio: recibirá un objeto de tipo domicilio y si no existe en la lista lo añadirá. 
#   EliminarDomicilio: recibirá un objeto de tipo domicilio y si existe debe eliminarlo de la lista. 
#   BuscarDomicilio: recibirá un nombre de calle y deberá devolver el objeto de tipo domicilio si existe en la lista.

class DomiciliosPersona:
    def __init__(self, NombrePersona, DNIPersona):
        self.ListaDomicilios = []
        self.NombrePersona = NombrePersona
        self.DNIPersona = DNIPersona

    def AnyadirDomicilio(self, domicilio):
        if domicilio not in self.ListaDomicilios:
            self.ListaDomicilios.append(domicilio)
        else:
            print(f"El domicilio ya existe en la lista.")

    def EliminarDomicilio(self, domicilio):
        if domicilio in self.ListaDomicilios:
            self.ListaDomicilios.remove(domicilio)
        else:
            print(f"El domicilio no está en la lista.")

    def BuscarDomicilio(self, nombre_calle):
        for domicilio in self.ListaDomicilios:
            if domicilio.NombreCalle == nombre_calle:
                return domicilio
        print(f"No se encontró ningún domicilio en la calle {nombre_calle}.")
        return None

domicilio1 = Domicilio(TipoVia="Calle", NombreCalle="Gran Vía", Numero="123", Puerta="A",
                       Piso="2", CP="28001", Ciudad="Madrid", Provincia="Comunidad de Madrid")
domicilio2 = Domicilio(TipoVia="Avenida", NombreCalle="Principal", Numero="456", Puerta="B",
                       Piso="1", CP="28002", Ciudad="Madrid", Provincia="Comunidad de Madrid")

persona = DomiciliosPersona(NombrePersona="Juan Pérez", DNIPersona="12345678A")
persona.AnyadirDomicilio(domicilio1)
persona.AnyadirDomicilio(domicilio2)

print(persona.BuscarDomicilio("Gran Vía"))  # Debería mostrar el objeto domicilio1
print(persona.BuscarDomicilio("Calle Inexistente"))  # Debería mostrar None