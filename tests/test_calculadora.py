import pytest
from src.calculadora import sumar, dividir, es_par


def test_dividir():
    assert dividir(10, 2) == 5
    
def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)

