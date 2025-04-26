import pytest
from Funcoes import soma, subtracao
from Funcoes import multiplicacao, potencia

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 2) == 3
    assert subtracao(10, 10) == 0
    assert subtracao(-1, -1) == 0

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(5, 0) == 0
    assert multiplicacao(-2, 3) == -6

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 1) == 5
    assert potencia(10, 0) == 1