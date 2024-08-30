from .familiar import Familiar
from .sin_conexion import SinConexion


class Pro(Familiar, SinConexion):
    """
    Clase que representa una membresía Pro, que hereda de Familiar y SinConexion.
    """

    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción a otro tipo si es válido.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada o la actual si el cambio no es válido.
        """
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
