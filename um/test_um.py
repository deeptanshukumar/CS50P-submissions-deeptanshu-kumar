from um import count

def test_normal():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um... w") == 1

def test_interrogation():
    assert count("um?") == 1

def test_words_with_um():
    assert count("yummy food thanks!") == 0

def test_many_words():
    assert count("Um, thanks, um, regular expressions is not hard") == 2
    assert count("Um? is this supposed to be ummm yummy?") == 1

def test_different_ponctuation():
    assert count("Um, thanks, um...") == 2


