from jar import Jar


def test_init():
    jar = Jar()
    jar.capacity == 12
    jar2 = Jar(6)
    jar2.capacity == 6


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(2)
    assert jar.size == 6
    jar.withdraw(4)
    assert jar.size == 2