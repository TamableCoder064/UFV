class Persona:
    def __init__(self, nombre, apellido1, apellido2, edad, nacionalidad, dni):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.dni = dni
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellidos: {self.apellido1} {self.apellido2}, DNI: {self.dni}'

jugador1=Persona('Santiago', 'Estalote', 'Mateos', 20, 'Español', '12345678Q')
print(jugador1)

class Jugador(Persona):
    def __init__(self, posicion, dorsal, numero_ficha, nombre, apellido1, apellido2, edad, nacionalidad, dni):
        super().__init__(nombre, apellido1, apellido2, edad, nacionalidad, dni)
        self.posicion = posicion
        self.dorsal = dorsal
        self.numero_ficha = numero_ficha

class Equipo:
    def __init__(self, nombre, estadio, entrenador, lista_jugadores):
        self.nombre = nombre
        self.estadio = estadio
        self.entrenador = entrenador
        self.lista_jugadores = lista_jugadores