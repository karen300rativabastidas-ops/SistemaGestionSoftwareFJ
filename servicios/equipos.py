from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)
        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Alquiler de equipos por {self.dias} días"