from um import count

def test_one():
    assert count("um") == 1

def test_two():
    assert count("tummy") == 0

def test_three():
    assert count("tu uM im um") == 2

def test_four():
    assert count("") == 0