# Electricity Consumption Calculator

A Python command-line application that helps users estimate electricity consumption and costs for household appliances, compare appliances, and explore potential energy savings.

## Current Features

- Calculate daily, monthly, and yearly electricity consumption and costs.
- Add and view multiple appliances with their power and daily usage.
- Calculate total monthly electricity consumption and cost.
- Rank appliances by monthly electricity cost.
- Compare monthly electricity costs between two appliances.
- Estimate potential monthly savings by reducing daily appliance usage.
- Retrieve household electricity prices from the Eurostat API.
- Select between Czech Republic, Germany, and France.
- Automatically use the selected country's electricity price in calculations, comparisons, rankings, and savings simulations.
- Display the reporting period of retrieved electricity prices.
- Allow manual electricity price entry when no country has been selected.
- Navigate through an interactive command-line menu.

## Planned Features

- Improve input validation and error handling.
- Add automated tests for calculations and API integration.
- Improve documentation and add project diagrams.

## Inputs

- Appliance name.
- Appliance power in watts (W).
- Daily usage in hours.
- Electricity price per kWh (entered manually or retrieved from Eurostat).
- Country selection when using Eurostat.
- New daily usage hours for savings simulations.

## Installation and Usage

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Install the required dependency:

   ```bash
   python -m pip install requests
   ```

5. Run the application:

   ```bash
   python main.py
   ```

6. Follow the interactive menu to add appliances, view consumption summaries, compare appliances, calculate potential savings, or retrieve electricity prices.

## Electricity Price Data

Electricity prices are retrieved from the Eurostat dataset `nrg_pc_204`.

The application currently supports:

- Czech Republic (CZ).
- Germany (DE).
- France (FR).

The data represents household electricity prices in EUR/kWh, including taxes, for the annual consumption band of 2,500–4,999 kWh.

Eurostat publishes these prices periodically. They are statistical reference prices rather than real-time electricity tariffs or personalized electricity bills.

## Limitations

- Eurostat prices are historical statistical data, not live supplier tariffs.
- Only three countries are currently available through the country-selection menu.
- Appliance data is stored in memory and is not saved after closing the application.
- Monthly calculations assume 30 days.
- Yearly calculations assume 365 days.
- Input validation and error handling are not yet fully implemented.
- Electricity consumption estimates assume constant appliance power during the entered usage hours.
- Costs calculated using Eurostat prices are expressed in EUR.

## Project Status

Development in progress.

The core electricity calculator, multiple-appliance management, consumption summaries, appliance ranking, appliance comparison, savings simulation, and Eurostat API integration have been implemented.

Initial manual tests have been completed successfully.

Automated tests, improved error handling, diagrams, and additional documentation are planned.