from modulo.persona import Persona
import pytest

p01 : Persona = None
p02 : Persona = None

def setup_module(module):
    global p01
    p01  = Persona("ricardo","bedu")
    global p02 
    p02 = Persona("pancho","emilinano zapata")

def test_get_nombre():
    assert p01.get_nombre()

@pytest.mark.parametrize('p',[ (p01,) , (p02,) ])
def test_get_escuela(p:Persona):
    assert p.get_escuela()

@pytest.mark.parametrize('p',[ (p01,) , (p02,) ])
def test_descibe(p:Persona):
    assert p.describe()