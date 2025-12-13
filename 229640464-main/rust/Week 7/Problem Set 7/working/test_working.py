import pytest
from working import convert

def test_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        convert("0 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("10:60 to 5:00 PM")

def test_different_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

