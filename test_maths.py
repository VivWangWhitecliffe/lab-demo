import maths

def test_addition():
    assert maths.add(2, 3) == 5

def test_subtraction():
    assert maths.subtract(5, 3) == 2

def test_wrongsubtraction():
    assert maths.subtract(6, 4) == 2

def test_wrongmultiply():
    assert maths.mutiply(6, 4) == 2

def test_mutiply():
    assert maths.mutiply(6, 4) == 24