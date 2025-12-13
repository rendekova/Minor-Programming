import twttr
import pytest
from twttr import shorten


def test_hello():
    assert shorten("hello") == "hll"

def test_goodbye():
    assert shorten("goodbye") == "gdby"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_lowercase():
    assert shorten("hello") == "hll"

def test_empty_string():
    assert shorten("") == ""

def test_punctuation():
    assert shorten("Hello!") == "Hll!"

def test_no_vowels():
    assert shorten("brr") == "brr"

def test_numbers():
    assert shorten("01234") == "01234"

def test_raise_of_typeerror():
    with pytest.raises(TypeError):
        shorten(None)




