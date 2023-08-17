from project import check_calories, check_price, check_cmd
import pytest
def test_check_cmd():
    with pytest.raises(SystemExit):
        check_cmd()


def test_check_calories():
    assert check_calories(100) == "To all weight"
    assert check_calories(250) == "To 120 Kg"
    assert check_calories(350) == "To 100 Kg"
    assert check_calories(500) == "To 80 Kg"



def test_check_price():
    assert check_price(10) == "Low cost"
    assert check_price(20) == "Well cost"
    assert check_price(30) == "High cost"