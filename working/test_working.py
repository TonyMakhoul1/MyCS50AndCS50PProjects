from working import convert
import pytest
def test_one():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_two():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_three():
    with pytest.raises(ValueError):
        convert("9:66 AM to 5:00 PM")

def test_four():
    with pytest.raises(ValueError):
        convert("9:66 AM - 5:00 PM")

def test_five():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
