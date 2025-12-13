import pytest
from um import count


def test_um():
    assert count("hello, um, wrold") == 1

def test_multiple_um():
    assert count("um, um") == 2

def test_zero_um():
    assert count("hello, world") == 0

def test_case_insensitivity():
    assert count("Um, um, UM") == 3

def test_um_in_a_word():
    assert count("yummy, human") == 0


