from numb3rs import validate

def testone():
    assert ip == validate(124.5.6.4)

def testtwo():
    assert ip == validate(255.255.255.255)
    