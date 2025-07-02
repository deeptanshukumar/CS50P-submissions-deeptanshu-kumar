from twttr import shorten
import sys

def test_output():
    try:
        assert shorten("aeioukkk") == "kkk"
        assert shorten("AEIOUKKK") == "KKK"
        assert shorten("123aeioukkk") == "123kkk"
        assert shorten("hi, kk") == "h, kk"
    except AssertionError:
        sys.exit(1)

