def resta(a, b):
    """ Función que realiza una resta de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la resta
    """
    try:
        a = float(a)
        b = float(b)
        return a - b
    except (ValueError, TypeError):
        return None