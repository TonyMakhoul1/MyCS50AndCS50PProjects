from working import convert, not_am_pm

def test_one():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_two():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    