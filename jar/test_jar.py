from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity=12, size=0)
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(3)
    assert jar.size == 4

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.withdraw(1)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
