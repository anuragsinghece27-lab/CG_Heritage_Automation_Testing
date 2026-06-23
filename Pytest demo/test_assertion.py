def test_equality():
    page_title = 'Dashboard'
    assert page_title == 'Dashboard'

def test_with_custom_message():
    actual_count = 4
    expected_count = 5
    assert actual_count == expected_count, f'Expected {expected_count}, but got {actual_count}'

def test_membership():
    cart_items = ['Laptop', 'Mouse', 'Keyboard']
    assert 'Mouse' in cart_items