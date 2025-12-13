from numb3rs import validate

def test_validate_ips():
    assert validate("120.26.2.3") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ips_split():
    assert validate("120,36; 7") == False

def test_invalid_ips_parts():
    assert validate("120.26.3") == False
    assert validate("0.0.0.0.0") == False
    assert validate("256.256") == False

def test_invalid_ips_nonnumeric():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("abc.256.43.33") == False
    assert validate("2.3.4.a") == False

def test_invalid_ips_range():
    assert validate("257.35.32.6") == False
    assert validate("36.88.299.8") == False

def test_invalid_ips_zeros():
    assert validate("01.34.33.2") == False
    assert validate("36.205.3.001") == False
