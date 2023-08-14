from seasons import check_birth


def test_one():
    assert check_birth("2002-09-09") == ("2002", "09", "09")

def test_two():
    assert check_birth("2002-9-9") == None