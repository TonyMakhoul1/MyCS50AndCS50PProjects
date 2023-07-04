from fuel import convert, gauge
import pytest

def test_one():
    assert convert("2/4") == 50 and gauge(50) == "50%"

def test_two():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_three():
    with pytest.raises(ValueError):
        convert("Dog/Cat")

def test_four():
    assert convert("1/100") == 1 and gauge(1) == "E"

def test_five():
    assert convert("99/100") == 99 and gauge(99) == "F"