from twttr import shorten

def test_one():
    assert shorten("tony") == "tny"

def test_two():
    assert shorten("anto") == "nt"
