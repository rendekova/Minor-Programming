import bank
import pytest
from bank import value

def test_hello():
    assert value("hello") == 0

def test_how_are_you():
    assert value("how are you") == 20

def test_otherwise():
    assert value("bye") == 100

def test_numbers():
    assert value("01234") == 100

def test_uppercase():
    assert value("HELLO") == 0
