import pytest
from app.resta import resta

def test_resta():
    assert resta(2, 2) == 0
    
    
@pytest.mark.parametrize(
    "valor_1,valor_2,resultado",
    [
        (1,2,-1),
        (-1,-2,1),
        (4,6,resta(4,6))
     ]
)    
def test_resta_varios(valor_1,valor_2,resultado):
    assert resta(valor_1,valor_2)==resultado   