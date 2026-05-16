from modelos.servicio import Servicio

class Asesoria(Servicio):

    def __init__(self, nombre, precio_base, sesiones):
        super().__init__(nombre, precio_base)
        self.sesiones = sesiones

    def calcular_costo(self):
        return self.precio_base * self.sesiones

    def descripcion(self):
        return f"Asesoría especializada de {self.sesiones} sesiones"
    