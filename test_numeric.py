from numeric  import add, sub, div
import pytest

def test_add():
    assert add(5, 4) == 9
    assert add(5, 10) == 15
    assert add(10, 3) == 13

def test_sub():
    assert sub(5, 4) == 1
    assert sub (4, 5) == -1


def test_div():
    assert div(6, 3) == 2
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
