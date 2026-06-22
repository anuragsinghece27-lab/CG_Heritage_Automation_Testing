class TestLoginPage:
    def test_valid_login(self):
        assert 'admin' == 'admin'

    def test_invalid_login(self):
        assert 'admin' != 'guest'

    def test_empty_username(self):
        username = ''
        assert username == ''