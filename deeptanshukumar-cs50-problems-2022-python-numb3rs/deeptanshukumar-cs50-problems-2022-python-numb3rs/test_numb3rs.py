from numb3rs import validate


def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.275") == False
    assert validate("275.3.6.28") == False
