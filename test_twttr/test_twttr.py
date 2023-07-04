from twttr import shorten

def test_one():
    name = "TONY"
    assert shorten(name) == "TNY"

def test_two():
    name = "ANTO"
    assert shorten(name) == "NT"

def test_three():
    asser shorten("me") == "m"
