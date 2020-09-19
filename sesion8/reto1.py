from modulo.operaciones import promedio


def test_promedio():
    assert promedio(5,3,1) == 5
    assert promedio(5,3,1) == 3
    assert promedio(4,4) == 4