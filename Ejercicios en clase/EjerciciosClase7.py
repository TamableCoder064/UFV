# Crear la clase Padre1, que tenga un método Imprimir1 que muestre el texto 'Padre1 llamado'
# Crear la clase Padre2, que tenga también un método Imprimir2 que muestre el texto 'Padre2 llamado'
# Crear una clase hija llamada Hija, que herede de Padre1 y de Padre2, Imprimir1 e Imprimir2
# Instancia la clase y observa el resultado

class Padre1:
    def Imprimir1(self):
        print('Padre1 llamado')
class Padre2:
    def Imprimir2(self):
        print('Padre2 llamado')
class Hija(Padre1, Padre2):
    def Imprimir(self):
        self.Imprimir1()
        self.Imprimir2()

h1 = Hija()
h1.Imprimir()