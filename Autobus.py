from Vehiculo import Vehiculo
class Autobus(Vehiculo):
    def __init__(self, matricula, modelo, potencia, asientos):
        super().__init__(matricula, modelo, potencia)
        self.__asientos = asientos

    def get_asientos(self):
        return self.__asientos

    def __str__(self):
        return f'{super().__str__()}\nAsientos: {self.__asientos}'