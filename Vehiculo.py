class Vehiculo:
    def __init__(self, matricula, modelo, potencia):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__potencia = potencia

    def get_matricula(self):
        return self.__matricula

    def get_modelo(self):
        return self.__modelo

    def get_potencia(self):
        return self.__potencia

    def __str__(self):
        return f'Matricula: {self.__matricula}\nModelo: {self.__modelo}\nPotencia: {self.__potencia}'