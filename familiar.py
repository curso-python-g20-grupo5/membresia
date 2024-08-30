from .basica import Basica


class Familiar(Basica):
    """
    Clase que representa una membresía familiar.
    """

    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción a otro tipo si es válido.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada o la actual si el cambio no es válido.
        """
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        """
        Método para modificar el control parental (no implementado).
        """
        pass
