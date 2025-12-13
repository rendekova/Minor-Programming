from plates import is_valid
import pytest




def test_letters():
    assert is_valid ("AAA222") == True

def test_numbers():
    assert is_valid ("AAA22A") == False

def test_zero():
    assert is_valid ("AA022") == False

def test_spaces():
    assert is_valid ("A 22AA") == False



def test_lenght():
    assert is_valid ("A") == False

def test_check_two_letters():
    assert is_valid ("ABC1234") == False

def test_no_space_no_symbols():
    assert is_valid ("A34?2") == False

def test_only_letters():
    assert is_valid ("ABC") == True

def test_numbers_at_end():
    assert is_valid ("AB123") == True

def test_onenumericcharac_():
    assert is_valid ("123456") == False

def test_nopunctuation():
    assert is_valid("to@st") == False
