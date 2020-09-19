# reto2.py::metodo
# pytest -m int -v
from modulo.operaciones import promedio
import pytest

@pytest.mark.text
def test_promedio_int():
    assert promedio(4,4) == 4
    assert promedio(5,2,4) == 3
    assert promedio(4,2) == 1

@pytest.mark.numero
def test_promedio_float():
    assert promedio(4.2,1.3,5.5) == 4.0
    assert promedio(3.3,3.3,3.3) == 3.3


@pytest.mark.parametrize('numero1,numero2,resultado',[(8,8,8),(1,2,4),(3,4,3.5),(4,4,4),(6,3,1),(8,8,8),(1,1.2,4),(3,3.2,3.5),(4,4,4.5),(6,3,3)])
def test_promedio_parametrizado(numero1,numero2,resultado):
    assert promedio(numero1,numero2) == resultado