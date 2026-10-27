
"""Main entry point for the Electricity Consumption Calculator."""


from src.calculator import (
    calculate_daily_consumption,
    calculate_daily_cost,
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

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
