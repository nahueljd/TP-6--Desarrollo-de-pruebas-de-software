import pytest
from app.suma import suma


def test_suma():
    assert suma(1, 5) == 6


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado",
    [
        (1,2,3),
        (2,2,4),
        (2,"r",None),
        ("t","r",None),
        (2.4,1.2,suma(2.4,1.2)),
        (4,6,suma(4,6))
     ]
)
def test_suma_varios(valor_1,valor_2,resultado):
    assert suma(valor_1,valor_2)==resultado


   
