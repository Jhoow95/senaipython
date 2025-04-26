import pytest

from funcoes import multiplicacao

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(5, 0) == 0
    assert multiplicacao(-2, 3) == -6
     assert multiplicacao(0, 0) == 0
     assert multiplicacao(5, 1) == 5