
"""Main entry point for the Electricity Consumption Calculator."""

from src.calculator import calculate_daily_consumption, calculate_daily_cost


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


if __name__ == "__main__":
    main()
