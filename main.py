from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.sala import ReservaSala
from servicios.equipos import AlquilerEquipo
from servicios.asesoria import Asesoria
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

clientes = []
reservas = []

def registrar_operacion(texto):
    print(texto)

operaciones = [

    lambda: Cliente("Karen", "karen@gmail.com"),
    lambda: Cliente("", "correo.com"),
    lambda: Cliente("Juan", "juan@gmail.com"),

]

for operacion in operaciones:

    try:

        cliente = operacion()
        clientes.append(cliente)

        registrar_operacion(
            f"Cliente registrado: {cliente.mostrar()}"
        )

    except Exception as e:

        logging.error(e)

        registrar_operacion(
            f"Error registrando cliente: {e}"
        )

try:

    servicio1 = ReservaSala(
        "Sala VIP",
        100,
        3
    )

    servicio2 = AlquilerEquipo(
        "Computador",
        50,
        2
    )

    servicio3 = Asesoria(
        "Python",
        80,
        4
    )

    servicios = [servicio1, servicio2, servicio3]

except Exception as e:
    logging.error(e)

for cliente in clientes:

    for servicio in servicios:

        try:

            reserva = Reserva(cliente, servicio)

            resultado = reserva.procesar()

            reservas.append(reserva)

            registrar_operacion(resultado)

        except Exception as e:

            logging.error(e)

            registrar_operacion(
                f"Error en reserva: {e}"
            )

print("\nSistema ejecutado correctamente")