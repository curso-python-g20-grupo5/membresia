from abc import ABC, abstractmethod
from .basica import Basica
from .familiar import Familiar
from .sin_conexion import SinConexion
from .pro import Pro


class Membresia(ABC):
    """
    Clase base abstracta para representar diferentes tipos de membresías.

    Atributos:
    correo_suscriptor (str): Correo electrónico del suscriptor.
    numero_tarjeta (str): Número de tarjeta del suscriptor.
    """

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Inicializa una nueva instancia de la clase Membresia.

        Parámetros:
        correo_suscriptor (str): Correo electrónico del suscriptor.
        numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        """
        Devuelve el correo electrónico del suscriptor.
        """
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        """
        Devuelve el número de tarjeta del suscriptor.
        """
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Método abstracto para cambiar la suscripción a otro tipo de membresía.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada.
        """
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        """
        Crea una nueva instancia de membresía según el tipo deseado.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía.
        """

        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
