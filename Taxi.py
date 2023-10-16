from Vehiculo import Vehiculo
class Taxi(Vehiculo):
    def __init__(self, matricula, modelo, potencia, licencia):
        super().__init__(matricula, modelo, potencia)
        self.__licencia = licencia

    def get_licencia(self):
        return self.__licencia

    def __str__(self):
        return f'{super().__str__()}\nLicencia: {self.__licencia}'