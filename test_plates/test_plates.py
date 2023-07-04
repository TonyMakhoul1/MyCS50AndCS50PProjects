from plates import is_valid

def test_one():
    assert is_valid("s") == False

def test_two():
    assert is_valid("helloyarame") == False

def test_three():
    assert is_valid("123") == False

def test_four():
    assert is_valid("")