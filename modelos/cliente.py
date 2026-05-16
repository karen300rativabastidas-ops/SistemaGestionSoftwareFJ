from modelos.excepciones import ClienteError

class Cliente:

    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def mostrar(self):
        return f"{self.__nombre} - {self.__correo}"