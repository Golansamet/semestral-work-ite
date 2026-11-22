"""Automated tests for electricity consumption and cost calculations."""

from src.calculator import calculate_consumption_for_days, calculate_cost_for_days


def test_monthly_consumption():
    """Verify monthly electricity consumption for a 100 W appliance."""
    result = calculate_consumption_for_days(100, 5, 30)
    assert result == 15


def test_monthly_cost():
    """Verify monthly electricity cost using a known electricity price."""
    result = calculate_cost_for_days(100, 5, 0.30, 30)
    assert result == 4.5


def test_zero_hours():
    """Verify that an appliance with zero usage consumes no electricity."""
    result = calculate_consumption_for_days(100, 0, 30)
    assert result == 0


def test_yearly_consumption():
    """Verify yearly consumption for a 1000 W appliance."""
    result = calculate_consumption_for_days(1000, 2, 365)
    assert result == 730
