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
        