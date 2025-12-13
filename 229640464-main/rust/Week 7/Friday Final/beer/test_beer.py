import os
import beer

def test_count_beerquotes():
    quotes = beer.read_quotes("beer.txt")
    assert len(quotes) in [25]

def test_count_winequote():
    quotes = beer.read_quotes("wine.txt")
    assert len(quotes) in [25]
    assert quotes[1].find("Wine") > 0
    assert quotes[2].find("beerpong") > 0

def test_regex():
    a = "I'd blabla beer than drink nobeerpong."
    aa = "I'd blabla wine than drink nobeerpong."
    b = beer.change_beer_into_wine(a)
    assert b == aa
    a = "Beer beerbeerbeer Beer beer Ber bbeer wine"
    aa = "Wine beerbeerbeer Wine wine Ber bbeer wine"
    b = beer.change_beer_into_wine(a)
    assert b == aa

def test_main():
    try:
        os.remove("wine.txt")
    except:
        pass
    beer.main()
    test_count_winequote()
    t = beer.read_quotes("test_beer.py")
    assert len(t) == 28
