def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b


def dividir(a, b):
    """Retorna la división. Lanza error si b es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def es_par(numero):
    """Verifica si un número es par."""
    return numero % 2 == 0

