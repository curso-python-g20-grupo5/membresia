from .gratis import Gratis


def main():
    """
    Función principal para ejecutar el ejemplo de uso de las membresías.
    """
    g = Gratis("correo@prueba.cl", "123 456 789")
    print(type(g))  # Imprime el tipo de membresía (Gratis)

    # Cambiar membresía a Pro
    g = g.cambiar_suscripcion(4)
    print(type(g))  # Imprime el tipo de membresía (Pro)

    # Cambiar membresía a SinConexion
    g = g.cambiar_suscripcion(3)
    print(type(g))  # Imprime el tipo de membresía (SinConexion)


if __name__ == "__main__":
    main()
