
"""Functions for calculating electricity consumption and costs."""


def calculate_daily_consumption(power_watts, hours_per_day):
    """Calculate daily electricity consumption in kWh."""
    consumption = (power_watts * hours_per_day) / 1000
    return consumption

def calculate_daily_cost(power_watts, hours_per_day, price_per_kwh):
    """Calculate the daily electricity cost."""
    consumption = calculate_daily_consumption(power_watts, hours_per_day)
    cost = consumption * price_per_kwh
    return cost
