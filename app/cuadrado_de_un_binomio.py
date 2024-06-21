from app.suma import suma
""" Función que calcula el cuadrado de un binomio (a + b)^2

    Args:
        a (int/float): primer término del binomio
        b (int/float): segundo término del binomio

    Returns:
        int/float: resultado del cuadrado del binomio

    Raises:
        TypeError: Si alguno de los argumentos no es un número (int o float)
    """
def cuadrado_binomio(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos valores deben ser enteros o flotantes")
    return suma(a*a, suma(2*a*b, b*b))
