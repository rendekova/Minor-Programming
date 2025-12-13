import logic as l

def test_decrypt():
    assert l.decrypt(11, "dzxp dectyr") == "some string"
    assert l.decrypt(17, "Kyzj yrj & jfdv jy***p tyrij!") == "This has & some sh***y chars!"

def test_decrypt_h():
    assert l.decrypt(37, "dzxp dectyr") == "some string"
    assert l.decrypt(485, "Kyzj yrj & jfdv jy***p tyrij!") == "This has & some sh***y chars!"
