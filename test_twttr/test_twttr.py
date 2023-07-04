from twttr import shorten

def test_one():
    name = "TONY"
    assert shorten(name) == "TNY"

def test_two():
    name = "ANTO"
    assert shorten(name) == "NT"

def test_three():
    assert shorten("me") == "m"

def test_four():
    assert shorten("4") == "4"

def test_five():
    assert shorten("!") == "!"
    