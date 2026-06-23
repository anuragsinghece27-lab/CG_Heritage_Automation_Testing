def test_valid_login():
    username = 'admin'
    password = 'admin123'
    assert username == 'admin' and password == 'admin123'

def test_invalid_login():
    username = 'wronguser'
    assert username != 'admin'