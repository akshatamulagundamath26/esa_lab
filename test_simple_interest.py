from simple_interest import calculate_simple_interest


def test_simple_interest_basic():
    assert simple_interest(1000, 5, 2) == 100.0


def test_simple_interest_zero_time():
    assert simple_interest(1500, 10, 0) == 0.0


def test_simple_interest_decimal_values():
    assert simple_interest(2500, 7.5, 3) == 562.5