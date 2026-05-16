from modelos.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError("Costo inválido")

            self.confirmar()

            return f"""
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.descripcion()}
Costo: ${costo}
Estado: {self.estado}
"""

        except Exception as e:
            raise ReservaError("Error procesando reserva") from e