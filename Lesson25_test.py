import pytest

def summa(a, b):
    return a + b

# print(summa(2, 2))

def test_summa_positive():
    assert summa(2, 2) == 4

def test_summa_positive2():
    assert summa(3, 8) == 11

def test_summa_positive3():
    assert summa(-3, -8) == -11