from um import count

def test_one():
    assert count("um") == 1

def test_two():
    assert count("tummy") == 0

def test_three():
    assert count("tu um im um") == 2
