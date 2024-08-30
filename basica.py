from .membresia import Membresia
from .gratis import Gratis


class Basica(Membresia):
    """
    Clase que representa una membresía básica.
    """

    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Inicializa una nueva instancia de la membresía básica.

        Parámetros:
        correo_suscriptor (str): Correo electrónico del suscriptor.
        numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)

        # Se establece el número de días regalo según el tipo de membresía
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        """
        Cancela la suscripción actual y regresa a la membresía gratuita.

        Retorna:
        Gratis: Nueva instancia de membresía gratuita.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción a otro tipo si es válido.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada o la actual si el cambio no es válido.
        """
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
