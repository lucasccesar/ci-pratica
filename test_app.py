from app import *

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(3, 3) == 0

def test_py3_13func():
    assert py3_13func([1,2,3,4])
