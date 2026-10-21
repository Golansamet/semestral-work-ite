
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

def calculate_consumption_for_days(power_watts, hours_per_day, days):
    """Calculate electricity consumption in kWh for a given number of days."""
    daily_consumption = calculate_daily_consumption(power_watts, hours_per_day)
    return daily_consumption * days

def calculate_cost_for_days(power_watts, hours_per_day, price_per_kwh, days):
    """Calculate electricity cost for a given number of days."""
    consumption = calculate_consumption_for_days(power_watts, hours_per_day, days)
    return consumption * price_per_kwh
