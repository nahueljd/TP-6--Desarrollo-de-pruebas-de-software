def suma(a, b):
    """ Función que realiza una suma de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    try:
        a = float(a)
        b = float(b)
        return a + b
    except (ValueError, TypeError):
        return None