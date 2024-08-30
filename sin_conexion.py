from .basica import Basica


class SinConexion(Basica):
    """
    Clase que representa una membresía sin conexión.
    """

    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción a otro tipo si es válido.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada o la actual si el cambio no es válido.
        """
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        """
        Método para incrementar la cantidad máxima de dispositivos offline (no implementado).
        """
        pass
