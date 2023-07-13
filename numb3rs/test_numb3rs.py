from numb3rs import validate

def testone():
    assert validate("124.5.6.4") == True

def testtwo():
    assert validate("255.300.255.255") == False
