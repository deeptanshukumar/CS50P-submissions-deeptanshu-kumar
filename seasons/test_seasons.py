from seasons import convert
import pytest

def test_convert():
    assert convert("2021-01-22") == "Two million, thirty-six thousand, one hundred sixty minutes"
    assert convert("2020-01-22") == "Two million, five hundred sixty-three thousand, two hundred minutes"

def test_exit():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            convert("January 1, 1999")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Not a valid format."
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            convert("1997 June 24")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Not a valid format."
