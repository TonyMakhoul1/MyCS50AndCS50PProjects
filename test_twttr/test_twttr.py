from twttr import shorten

def test_one():
    name = "tony"
    assert shorten(name) == "tny"

def test_two():
    name = "anto"
    assert shorten(name) == "nt"
