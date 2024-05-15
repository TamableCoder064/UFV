# Definir la clase Calculadora.

# Crea un constructor con los atributos operador1 y operador2 inicializados a 0,
# y con __codigoOP inicializado con un número aleatorio.

# Crear el método Sumar que recib dos parámetros de entrada op1 y op2.
# Debe devolver el resultado de la operación de suma de ambos,
# concatenados con el código de la operación interna (__codigoOP).

# Crea una instancia del objeto Calculadora y llama al método Suma.

# Intenta imprimir el código de operación interna (__codigoOP) a través del objeto.

# Cambia la función Sumar por __Sumar y llámala a través del objeto.

# Ahora crear el método Operar, que recibirá tres parámetros de entrada, la operación que se quiere reallizar, op1 y op2.
# Si recibe un + debe llamar a la función interna __Sumar con el op1 y el op2, en caso de contrario lanzará una excepción indicando que no existe la operación.
# Actualizará el código de la operación interna.

import random
class Calculadora:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.__codigoOP = random.randint(0,100)
    def Sumar(self, op1, op2):
        return str(self.op1 + self.op2) + str (self.__codigoOP)
manuel = Calculadora()
# 'print(manuel.__codigoOP)' no se puede acceder es privado
manuel.Sumar(1,2)


class Calculadora:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.__codigoOP = random.randint(0,100)
    def __Sumar(self, op1, op2):
        return str(self.op1 + self.op2) + str (self.__codigoOP)
    def Operar(self, par1, par2, par3='+'):
        if par3 == '+':
            self.__Sumar(par1, par2)
        else:
            raise Exception('No existe la operación')
            self.__codigoOP = random.randint(0,100)