from .membresia import Membresia


class Gratis(Membresia):
    """
    Clase que representa una membresía gratuita.
    """

    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción a otro tipo si es válido.

        Parámetros:
        nueva_membresia (int): Tipo de nueva membresía deseada.

        Retorna:
        Membresia: Nueva instancia de la membresía cambiada o la actual si el cambio no es válido.
        """
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
