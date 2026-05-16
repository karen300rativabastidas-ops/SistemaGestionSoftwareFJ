from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)
        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"