from bank import value

def test_one():
    assert value("hello") == 0

def test_two():
    assert value("Hello") == 0

def test_three():
    assert value("Hany") == 20

def test_four():
    assert value("ana") == 100
