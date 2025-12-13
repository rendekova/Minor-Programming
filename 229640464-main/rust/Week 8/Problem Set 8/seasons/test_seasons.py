from datetime import date
from seasons import min_lived

def test_same_day():
    assert min_lived(date(2025, 10, 18), date(2025, 10, 18)) == 0

def test_leap_year():
    # 366 * 24 * 60 = 527040
    assert min_lived(date(2020, 1, 1), date(2021, 1, 1)) == 527040

def test_year_nonleap():
    # 365 * 24 * 60 = 525600
    assert min_lived(date(2024, 10, 18), date(2025, 10, 18)) == 525600

def test_day():
    assert min_lived(date(2025, 10, 17), date(2025, 10, 18)) == 1440
