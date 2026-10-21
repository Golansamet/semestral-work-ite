
"""Main entry point for the Electricity Consumption Calculator."""


from src.calculator import (
    calculate_daily_consumption,
    calculate_daily_cost,
    calculate_consumption_for_days,
    calculate_cost_for_days,
)



def main():
    """Run the electricity calculator."""
    print("=== Electricity Consumption Calculator ===")

    power = float(input("Enter appliance power (W): "))
    hours = float(input("Enter daily usage (hours): "))
    price = float(input("Enter electricity price per kWh: "))

    consumption = calculate_daily_consumption(power, hours)
    cost = calculate_daily_cost(power, hours, price)

    print(f"\nDaily consumption: {consumption:.2f} kWh")
    print(f"Daily cost: {cost:.2f}")

    monthly_consumption = calculate_consumption_for_days(power, hours, 30)
    yearly_consumption = calculate_consumption_for_days(power, hours, 365)

    monthly_cost = calculate_cost_for_days(power, hours, price, 30)
    yearly_cost = calculate_cost_for_days(power, hours, price, 365)

    print(f"\nMonthly consumption: {monthly_consumption:.2f} kWh")
    print(f"Monthly cost: {monthly_cost:.2f}")
    print(f"\nYearly consumption: {yearly_consumption:.2f} kWh")
    print(f"Yearly cost: {yearly_cost:.2f}")


if __name__ == "__main__":
    main()
