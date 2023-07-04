from plates import is_valid

def test_one():
    assert is_valid("s") == False

def test_two():
    assert is_valid("helloyarame") == False

def test_three():
    assert is_valid("1imtony") == False

def test_four():
    assert is_valid("cs05t") == False

def test_five():
    assert is_valid("cs50.t") == False

def test_six():
    assert is_valid("cscit") == True

def test_seven():
    assert is_valid("2tony") == False

def test_eight():
    assert is_valid("01234") == False

def test_nine():
    assert is_valid("cs50") == True