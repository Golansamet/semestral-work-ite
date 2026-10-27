
# Electricity Consumption Calculator

A Python command-line application that helps users estimate electricity consumption and costs for household appliances.

## Current Features

- Calculate daily, monthly, and yearly electricity consumption and costs.
- Add multiple appliances with their power and daily usage.
- View all added appliances.
- Calculate total monthly electricity consumption and cost.
- Rank appliances by monthly electricity cost.
- Navigate through an interactive command-line menu.

## Planned Features

- Compare electricity costs between appliances.
- Estimate potential savings by reducing daily usage.
- Retrieve the latest available electricity prices by country using the Eurostat API.
- Improve input validation and error handling.

## Inputs

- Appliance name.
- Appliance power in watts (W).
- Daily usage in hours.
- Electricity price per kWh.

## Installation and Usage

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

   python main.py

5. Follow the menu instructions to add appliances, view consumption summaries, and rank appliances.

No external Python dependencies are currently required.

## Limitations

- Electricity prices must currently be entered manually.
- Appliances are stored in memory and are not saved after closing the program.
- Monthly calculations assume 30 days.
- Yearly calculations assume 365 days.
- Input validation is not yet implemented.

## Project Status

Development in progress.

The basic calculator, multiple-appliance management, monthly consumption summary, and appliance ranking are implemented.

Automated tests, diagrams, additional documentation, and further features are planned.
