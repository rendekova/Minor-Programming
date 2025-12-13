import pytest
from fuel import convert, gauge


# Covert testing
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("4/4") == 100

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3.5/4")
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("a/b")

def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/5")
    with pytest.raises(ValueError):
        convert("3/-5")


#Gauge testing
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

