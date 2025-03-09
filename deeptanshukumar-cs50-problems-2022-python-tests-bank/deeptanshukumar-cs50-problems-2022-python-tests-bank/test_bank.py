from bank import value
import sys

def test_value():
    try:
        assert value("hello, jane") == 0
        assert value("hi, jane") == 20
        assert value("hiya, jane") == 20
        assert value("wassup, jane") == 100
        assert value("Hello, jane") == 0
    except AssertionError:
        sys.exit(1)
