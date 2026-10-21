
"""Functions for calculating electricity consumption and costs."""


def calculate_daily_consumption(power_watts, hours_per_day):
    """Calculate daily electricity consumption in kWh."""
    consumption = (power_watts * hours_per_day) / 1000
    return consumption
