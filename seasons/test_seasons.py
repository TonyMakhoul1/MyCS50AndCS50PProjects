from seasons import check_birth
import pytest

def test_one():
    assert check_birth("2002-09-09") == ("2002", "09", "09")

def test_two():
    with pytest.raises(ValueError):
        check_birth("2002-2-2")