class Vehiculo:
    def __init__(self, matricula, tiempo_entrada):
        self.matricula = matricula
        self.tiempo_entrada = tiempo_entrada

class Moto(Vehiculo):
    def __init__(self, matricula, tiempo_entrada):
        super().__init__(matricula, tiempo_entrada)
        self.tipo = 'moto'

class Coche(Vehiculo):
    def __init__(self, matricula, tiempo_entrada):
        super().__init__(matricula, tiempo_entrada)
        self.tipo = 'coche'

class Furgoneta(Vehiculo):
    def __init__(self, matricula, tiempo_entrada):
        super().__init__(matricula, tiempo_entrada)
        self.tipo = 'furgoneta'

class Plaza:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.vehiculo = None

class Parking:
    def __init__(self, num_plazas_moto, num_plazas_coche, num_plazas_furgoneta):
        self.plazas = {
            'moto': [Plaza(i, 'moto') for i in range(1, num_plazas_moto + 1)],
            'coche': [Plaza(i, 'coche') for i in range(1, num_plazas_coche + 1)],
            'furgoneta': [Plaza(i, 'furgoneta') for i in range(1, num_plazas_furgoneta + 1)]
        }
        self.historico = []
        self.ingresos = 0.0
        self.tiempo_actual = 0

    def avanzar_tiempo(self, minutos):
        self.tiempo_actual += minutos

    def aparcar(self, matricula, tipo):
        vehiculo = None
        if tipo == 'moto':
            vehiculo = Moto(matricula, self.tiempo_actual)
        elif tipo == 'coche':
            vehiculo = Coche(matricula, self.tiempo_actual)
        elif tipo == 'furgoneta':
            vehiculo = Furgoneta(matricula, self.tiempo_actual)
        else:
            print("Tipo de vehículo no válido.")
            return None
        
        for plaza in self.plazas[tipo]:
            if plaza.vehiculo is None:
                plaza.vehiculo = vehiculo
                print(f'Vehículo {matricula} aparcado en plaza {tipo} número {plaza.numero}')
                return plaza.numero
        print(f'No hay plazas disponibles para {tipo}')
        return None

    def sacar_vehiculo(self, matricula):
        for tipo, plazas_tipo in self.plazas.items():
            for plaza in plazas_tipo:
                if plaza.vehiculo and plaza.vehiculo.matricula == matricula:
                    vehiculo = plaza.vehiculo
                    plaza.vehiculo = None
                    tiempo_salida = self.tiempo_actual
                    minutos_estacionado = tiempo_salida - vehiculo.tiempo_entrada
                    coste = self.calcular_coste(vehiculo.tipo, minutos_estacionado)
                    self.historico.append({
                        'matricula': vehiculo.matricula,
                        'tipo': vehiculo.tipo,
                        'tiempo_entrada': vehiculo.tiempo_entrada,
                        'tiempo_salida': tiempo_salida,
                        'coste': coste
                    })
                    self.ingresos += coste
                    print(f'Vehículo {matricula} retirado de plaza {tipo} número {plaza.numero}. Coste: {coste:.2f} €')
                    return coste
        print(f'No se encontró el vehículo con matrícula {matricula}')
        return None

    def calcular_coste(self, tipo, minutos):
        tarifas = {'moto': 0.41, 'coche': 0.53, 'furgoneta': 0.63}
        if minutos <= 180:
            return minutos * tarifas[tipo]
        else:
            return 180 * tarifas[tipo] + (minutos - 180) * 1.42

    def estado_parking(self):
        estado = {}
        for tipo, plazas_tipo in self.plazas.items():
            libres = sum(1 for plaza in plazas_tipo if plaza.vehiculo is None)
            total = len(plazas_tipo)
            estado[tipo] = {'libres': libres, 'ocupadas': total - libres, 'porcentaje_libres': int(libres / total * 100)}
        return estado

    def mostrar_estado(self):
        estado = self.estado_parking()
        for tipo, info in estado.items():
            print(f'{tipo.capitalize()} - Libres: {info["libres"]}, Ocupadas: {info["ocupadas"]}, Porcentaje libres: {info["porcentaje_libres"]}%')

    def mostrar_ingresos(self):
        print(f'Ingresos totales del día: {self.ingresos:.2f} €')

def menu():
    parking = Parking(num_plazas_moto=10, num_plazas_coche=20, num_plazas_furgoneta=5)

    while True:
        print("\nMenú de opciones:")
        print("A) Aparcar vehículo")
        print("B) Sacar vehículo")
        print("C) Mostrar estado del parking")
        print("D) Mostrar ingresos del día")
        print("E) Avanzar tiempo")
        print("F) Cierre de turno")
        opcion = input("Seleccione una opción: ").lower()

        if opcion == 'a':
            matricula = input("Introduzca la matrícula del vehículo: ").upper()
            tipo = input("Introduzca el tipo de vehículo (moto/coche/furgoneta): ").lower()
            if tipo in ['moto', 'coche', 'furgoneta']:
                parking.aparcar(matricula, tipo)
            else:
                print("Tipo de vehículo no válido.")
        elif opcion == 'b':
            matricula = input("Introduzca la matrícula del vehículo: ").upper()
            parking.sacar_vehiculo(matricula)
        elif opcion == 'c':
            parking.mostrar_estado()
        elif opcion == 'd':
            parking.mostrar_ingresos()
        elif opcion == 'e':
            minutos = int(input("Introduzca los minutos a avanzar: "))
            parking.avanzar_tiempo(minutos)
        elif opcion == 'f':
            print("Cierre de turno:")
            parking.mostrar_ingresos()
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()