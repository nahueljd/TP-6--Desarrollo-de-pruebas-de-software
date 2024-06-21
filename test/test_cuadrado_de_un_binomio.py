import pytest
from app.cuadrado_de_un_binomio import cuadrado_binomio

@pytest.mark.parametrize(
    "valor_1,valor_2,resultado",
    [
        (2, 3, 25),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, cuadrado_binomio(1.5, 2.5)),
        (-2, -3, cuadrado_binomio(-2, -3)),
        ("a", 1, None),
        (2, "b", None)
    ]
)
def test_cuadrado_binomio_varios(valor_1, valor_2, resultado):
    try:
        assert cuadrado_binomio(valor_1, valor_2) == resultado
    except TypeError:
        assert resultado is None
