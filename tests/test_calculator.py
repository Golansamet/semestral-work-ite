from src.calculator import calculate_consumption_for_days, calculate_cost_for_days


def test_monthly_consumption():
    result = calculate_consumption_for_days(100, 5, 30)

    assert result == 15

def test_monthly_cost():
    result = calculate_cost_for_days(100, 5, 30, 0.30)

    assert result == 4.5

def test_zero_hours():
    result = calculate_consumption_for_days(100, 0, 30)

    assert result == 0

def test_yearly_consumption():
    result = calculate_consumption_for_days(1000, 2, 365)

    assert result == 730
