
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
- Validate appliance input, including non-empty names, numeric values, positive power, and daily usage between 0 and 24 hours.
- Handle invalid appliance input without crashing the application.
- Run automated calculation tests using pytest.

## Automated Tests

The project includes four automated tests using pytest.

The tests cover:

1. Monthly electricity consumption calculation.
2. Monthly electricity cost calculation.
3. Zero daily usage.
4. Yearly electricity consumption calculation.

All four tests have passed successfully.

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

## Running Automated Tests

Install pytest:

```bash
python -m pip install pytest
```

Run all automated tests from the project directory:

```bash
python -m pytest -v
```

The tests are located in:

```text
tests/test_calculator.py
```

The current test suite contains four tests, all of which have passed successfully.

## Electricity Price Data

Electricity prices are retrieved from the Eurostat dataset `nrg_pc_204`.

The application currently supports:

- Czech Republic (CZ).
- Germany (DE).
- France (FR).

The data represents household electricity prices in EUR/kWh, including taxes, for the annual consumption band of 2,500–4,999 kWh.

Eurostat publishes these prices periodically. They are statistical reference prices rather than real-time electricity tariffs or personalized electricity bills.

## Project Structure

```text
semestral-work-ite/
├── src/
│   ├── calculator.py
│   └── electricity_prices.py
├── tests/
│   └── test_calculator.py
├── .gitignore
├── main.py
└── README.md
```

- `main.py` — Interactive command-line menu and appliance management.
- `src/calculator.py` — Electricity consumption and cost calculations.
- `src/electricity_prices.py` — Eurostat API integration.
- `tests/test_calculator.py` — Automated calculation tests.
- `README.md` — Project documentation.

## Limitations

- Eurostat prices are historical statistical data, not live supplier tariffs.
- Only three countries are currently available through the country-selection menu.
- Appliance data is stored in memory and is not saved after closing the application.
- Monthly calculations assume 30 days.
- Yearly calculations assume 365 days.
- Input validation has been implemented for adding appliances, but is not yet comprehensive across all menu options.
- Automated tests currently cover calculation functions, not Eurostat API integration.
- Electricity consumption estimates assume constant appliance power during the entered usage hours.
- Costs calculated using Eurostat prices are expressed in EUR.

## Planned Improvements

- Extend input validation and error handling to additional menu options.
- Add automated tests for Eurostat API integration.
- Add a simple project architecture diagram.

## Project Status

The core functionality has been implemented.

Completed components include:

- Electricity consumption and cost calculator.
- Multiple-appliance management.
- Monthly consumption summaries.
- Appliance ranking and comparison.
- Potential savings simulation.
- Eurostat API integration.
- Input validation for adding appliances.
- Four automated calculation tests using pytest.
- Project documentation and GitHub version control.

Manual tests have been completed successfully, including retrieving electricity prices from Eurostat and handling invalid appliance input.

All four automated calculation tests have passed.

The project is undergoing final review and preparation for submission and presentation.
