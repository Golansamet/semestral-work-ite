
"""Main entry point for the Electricity Consumption Calculator."""



from src.calculator import (
    calculate_consumption_for_days,
    calculate_cost_for_days,
)




def add_appliance(appliances):
    """Add a new appliance to the list."""
    name = input("Enter appliance name: ")
    power = float(input("Enter appliance power (W): "))
    hours = float(input("Enter daily usage (hours): "))

    appliance = {
        "name": name,
        "power": power,
        "hours": hours
    }

    appliances.append(appliance)
    print(f"{name} added successfully!")

def show_menu():
    """Display the main menu."""
    print("\n=== Electricity Consumption Calculator ===")
    print("1. Add appliance")
    print("2. View appliances")
    print("3. Monthly consumption summary")
    print("4. Rank appliances by monthly cost")
    print("5. Compare two appliances")
    print("6. Calculate potential savings")
    print("0. Exit")

def view_appliances(appliances):
    """Display all appliances in the list."""
    if not appliances:
        print("No appliances added yet.")
        return

    print("\n=== Your Appliances ===")

    for appliance in appliances:
        print(f"Name: {appliance['name']}")
        print(f"Power: {appliance['power']} W")
        print(f"Daily usage: {appliance['hours']} hours")
        print("--------------------")


def show_consumption_summary(appliances, price_per_kwh):
    """Display monthly consumption and costs for all appliances."""
    if not appliances:
        print("No appliances added yet.")
        return

    total_consumption = 0
    total_cost = 0

    print("\n=== Monthly Consumption Summary ===")

    for appliance in appliances:
        consumption = calculate_consumption_for_days(
            appliance["power"], appliance["hours"], 30
        )
        cost = consumption * price_per_kwh

        print(f"{appliance['name']}: {consumption:.2f} kWh, {cost:.2f}")

        total_consumption += consumption
        total_cost += cost

    print("--------------------")
    print(f"Total consumption: {total_consumption:.2f} kWh")
    print(f"Total monthly cost: {total_cost:.2f}")

def rank_appliances(appliances, price_per_kwh):
    """Display appliances ranked by monthly electricity cost."""
    if not appliances:
        print("No appliances added yet.")
        return

    ranked = sorted(
        appliances,

        key=lambda item: calculate_cost_for_days(
            item["power"], item["hours"], price_per_kwh, 30
        ),

        reverse=True
    )

    print("\n=== Appliances Ranked by Monthly Cost ===")

    for appliance in ranked:
        cost = calculate_cost_for_days(
            appliance["power"], appliance["hours"], price_per_kwh, 30
        )
        print(f"{appliance['name']}: {cost:.2f}")

def compare_appliances(first, second, price_per_kwh):
    """Compare the monthly electricity costs of two appliances."""
    first_cost = calculate_cost_for_days(
        first["power"], first["hours"], price_per_kwh, 30
    )
    second_cost = calculate_cost_for_days(
        second["power"], second["hours"], price_per_kwh, 30
    )

    print(f"\n{first['name']}: {first_cost:.2f}")
    print(f"{second['name']}: {second_cost:.2f}")
    print(f"Monthly cost difference: {abs(first_cost - second_cost):.2f}")

def calculate_savings(power_watts, current_hours, new_hours, price_per_kwh):
    """Calculate monthly savings from reducing daily appliance usage."""
    current_cost = calculate_cost_for_days(
        power_watts, current_hours, price_per_kwh, 30
    )
    new_cost = calculate_cost_for_days(
        power_watts, new_hours, price_per_kwh, 30
    )

    return current_cost - new_cost

def main():
    """Run the electricity calculator menu."""
    appliances = []

    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            add_appliance(appliances)

        elif choice == "2":
            view_appliances(appliances)

        elif choice == "3":
            if appliances:
                price = float(input("Enter electricity price per kWh: "))
                show_consumption_summary(appliances, price)
            else:
                print("No appliances added yet.")


        elif choice == "4":
            if appliances:
                price = float(input("Enter electricity price per kWh: "))
                rank_appliances(appliances, price)
            else:
                print("No appliances added yet.")


        elif choice == "5":
            if len(appliances) < 2:
                print("Please add at least two appliances.")
            else:
                for i, appliance in enumerate(appliances, start=1):
                    print(f"{i}. {appliance['name']}")

                first_index = int(input("Select first appliance: ")) - 1
                second_index = int(input("Select second appliance: ")) - 1
                price = float(input("Enter electricity price per kWh: "))

                compare_appliances(
                    appliances[first_index],
                    appliances[second_index],
                    price
                )

        elif choice == "6":
            if not appliances:
                print("No appliances added yet.")
            else:
                for i, appliance in enumerate(appliances, start=1):
                    print(f"{i}. {appliance['name']}")

                index = int(input("Select appliance: ")) - 1
                selected = appliances[index]

                new_hours = float(input("Enter new daily usage (hours): "))
                price = float(input("Enter electricity price per kWh: "))

                savings = calculate_savings(
                    selected["power"],
                    selected["hours"],
                    new_hours,
                    price
                )

                print(f"Potential monthly savings: {savings:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
