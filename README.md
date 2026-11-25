# EnergyWise — Electricity Consumption Calculator

**EnergyWise** is a Python project for estimating household electricity consumption, comparing appliance costs, and exploring how changes in daily usage can reduce electricity expenses.

The project offers two ways to use the same calculation logic:

- **Streamlit dashboard (`app.py`)** — a visual, single-page interface with summary cards, an appliance-cost chart, appliance management, an electricity-price selector, and a savings simulator.
- **Command-line application (`main.py`)** — an interactive terminal menu for appliance management, monthly summaries, rankings, comparisons, savings estimates, and Eurostat price retrieval.

Both interfaces support manually entered electricity prices and household electricity price data retrieved from the **Eurostat API**.

## Purpose

The purpose of this project is to help users understand how much electricity their household appliances consume, what that consumption costs, and how daily usage affects their bills.

Users can identify appliances with higher estimated operating costs, compare consumption, and calculate potential savings from reducing usage hours.

## Features

### Streamlit dashboard

- Display **monthly consumption**, **monthly cost**, and **potential savings** in three summary cards.
- Add household appliances with a name, power in watts, and hours used per day.
- Display a **monthly cost-by-appliance bar chart** (up to the five highest-cost appliances).
- Show up to three appliances directly on the dashboard, with a **View All** dialog to manage the complete list when more than three have been added.
- Remove appliances and immediately update totals and the chart.
- Open a **Quick Calculator** dialog to estimate consumption and cost without adding an appliance.
- Simulate monthly savings by selecting an appliance and reducing its daily usage hours.
- Enter a manual electricity price or retrieve a Eurostat reference price for Czech Republic, Germany, or France.
- Display the Eurostat reporting period and recalculate costs using the selected price.
- Use a full-width dashboard with no separate sidebar or top navigation.

### Command-line application

- Add and view multiple household appliances.
- Calculate monthly electricity consumption in kWh and estimated monthly costs.
- Display total monthly consumption and cost.
- Rank appliances by monthly electricity cost.
- Compare the monthly costs of two appliances.
- Estimate potential monthly savings from reduced daily usage.
- Retrieve household electricity prices from Eurostat and use them for later calculations.
- Validate appliance names, power, hours of usage, prices, and selections.

### Testing and documentation

- Four automated calculation tests using `pytest`.
- Testing documentation in [`docs/tests.md`](docs/tests.md).
- Activity and sequence diagrams in [`docs/diagrams/`](docs/diagrams/).

## Inputs and Outputs

### Inputs

- Appliance name.
- Appliance power in watts (W).
- Daily usage in hours (0–24 hours).
- Electricity price per kWh, entered manually or retrieved from Eurostat.
- Country selection: Czech Republic, Germany, or France.
- Appliance selection and reduced daily hours for savings simulations.
- Two appliance selections for comparison in the CLI.

### Outputs

- Estimated electricity consumption in kilowatt-hours (kWh).
- Estimated electricity costs in the selected price's currency.
- Total monthly consumption and cost summaries.
- Monthly cost by appliance, including a chart in the dashboard.
- Appliance rankings and cost comparisons in the CLI.
- Potential monthly electricity savings.
- Eurostat reference price and reporting period.
- Messages for invalid inputs or unavailable price data.

## Calculation Logic

Electricity consumption is calculated using:

**Consumption (kWh) = Power (W) / 1000 × Hours**

Electricity cost is calculated using:

**Cost = Consumption (kWh) × Electricity price per kWh**

Monthly calculations assume **30 days**. Yearly calculations assume **365 days**.

### Example

Consider a television with:

- Power: 100 W
- Daily usage: 5 hours
- Electricity price: 0.30 per kWh

Daily consumption:

```text
100 / 1000 × 5 = 0.5 kWh
```

Monthly consumption:

```text
0.5 × 30 = 15 kWh
```

Monthly cost:

```text
15 × 0.30 = 4.50
```

The same calculation logic is reused for appliance rankings, comparisons, the dashboard, and savings simulations. The currency of a manually entered price is determined by the user; Eurostat prices are in EUR.

## How the Program Works

### Streamlit dashboard (`app.py`)

1. Start the dashboard and add appliances using **+ Add Appliance**.
2. The application calculates monthly consumption and cost for each appliance and updates the summary cards and chart.
3. Use **Quick Calculator** for a one-off calculation without saving an appliance.
4. Use **Electricity Price** to enter a manual rate or select a country and click **Get Price** to load Eurostat data.
5. Use **Potential Energy Savings** to select an appliance, enter fewer hours per day, and click **Calculate**.
6. Remove appliances directly from the dashboard or use **View All** to manage the full list.

The dashboard stores appliances, settings, and simulation results in Streamlit session state while the application session remains active. Data is not saved to a database or file.

### Command-line program (`main.py`)

1. Start the program to display the interactive menu.
2. Add an appliance or choose an operation.
3. Enter the required inputs; the program validates them.
4. The appropriate calculation or Eurostat retrieval function runs.
5. View the result and return to the main menu until exiting.

When a valid country price is retrieved, the program uses it for subsequent calculations. The CLI also supports manually entered prices.

## Program Diagrams

These diagrams document the **original command-line program** and its interaction with the Eurostat API. The Streamlit dashboard was added later and uses the same underlying calculation and price-retrieval modules.

### Activity Diagram

The activity diagram illustrates the command-line program flow, including menu navigation, input validation, calculations, and returning to the main menu.

![Activity Diagram](docs/diagrams/activity_diagram.png)

### Sequence Diagram

The sequence diagram illustrates the interaction between the user, application, and Eurostat API when retrieving electricity prices.

![Sequence Diagram](docs/diagrams/sequence_diagram.png)

The diagram files are stored in `docs/diagrams/`.

## Installation and Usage

### Requirements

- Python 3.10 or newer (tested locally with Python 3.12)
- Packages listed in `requirements.txt`, including `streamlit`, `requests`, and `pytest`
- Internet connection for fetching Eurostat data (manual-price calculations work without an API request)

### Installation

1. Clone or download the repository:

   ```bash
   git clone https://github.com/Golansamet/semestral-work-ite.git
   cd semestral-work-ite
   ```

2. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Run the Streamlit dashboard

From the project directory:

```bash
python -m streamlit run app.py
```

Open the local address shown by Streamlit, usually **http://localhost:8501**, in a browser. Keep that terminal running while using the dashboard; press **Ctrl+C** in the terminal to stop it.

### Run the command-line application

From the project directory:

```bash
python main.py
```

The following interactive menu will appear:

```text
=== Electricity Consumption Calculator ===
1. Add appliance
2. View appliances
3. Monthly consumption summary
4. Rank appliances by monthly cost
5. Compare two appliances
6. Calculate potential savings
7. Select country and retrieve electricity price
0. Exit
```

Follow the terminal prompts. Choose option `0` to exit.

## Electricity Price Data

The project retrieves household electricity price data from Eurostat dataset **`nrg_pc_204`**.

Supported countries:

- Czech Republic (`CZ`)
- Germany (`DE`)
- France (`FR`)

The project's query uses household electricity prices in **EUR/kWh**, including taxes, for the annual consumption band of **2,500–4,999 kWh**. It selects the latest reporting period available from the queried dataset.

**Eurostat publishes periodic statistical reference prices. They are not real-time supplier tariffs or personalized electricity bills.**

When a Eurostat price is active, calculated costs appear in **EUR**. A manually entered price uses whatever currency unit the user intends.

In the dashboard, **Get Price** must be used to retrieve a price for the selected country. If no applicable Eurostat price is available, calculations fall back to the saved manual rate.

## Automated Tests

The project uses **pytest**. The automated tests are stored in `tests/test_calculator.py`.

Four tests cover:

1. Monthly electricity consumption calculation.
2. Monthly electricity cost calculation.
3. Zero daily usage.
4. Yearly electricity consumption calculation.

These tests compare calculated results against known expected values.

### Run all tests

```bash
python -m pytest -q
```

Alternatively, run the test suite with verbose output or the project's test runner:

```bash
python -m pytest -v
python test_main.py
```

**Last local verification (25 November 2026): 4 tests passed using `python test_main.py`.**

### Testing documentation

The testing strategy, rationale, example inputs and outputs, manual test scenarios, and limitations are documented in **[Testing Documentation](docs/tests.md)**.

## Input Validation

The project includes input validation and error handling for common user mistakes.

Examples include:

- Rejecting empty appliance names.
- Rejecting non-numeric or non-positive appliance power values.
- Restricting daily appliance usage to 0–24 hours.
- Rejecting invalid appliance selections.
- Rejecting non-numeric or negative manual electricity prices.
- Preventing savings simulations from increasing usage hours.

In the CLI, invalid inputs display a message and generally return the user to the menu. In the dashboard, Streamlit widgets enforce input ranges and show validation messages where applicable. If Eurostat data cannot be retrieved, the dashboard continues using the manual rate.

## Project Structure

```text
semestral-work-ite/
├── .streamlit/
│   └── config.toml
├── src/
│   ├── calculator.py
│   └── electricity_prices.py
├── tests/
│   └── test_calculator.py
├── docs/
│   ├── diagrams/
│   │   ├── activity_diagram.png
│   │   └── sequence_diagram.png
│   └── tests.md
├── app.py
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Main Files

- `app.py` — Streamlit dashboard, appliance-management dialogs, cost chart, savings simulator, and electricity-price controls.
- `.streamlit/config.toml` — Streamlit theme configuration.
- `main.py` — Command-line interface, appliance management, menu navigation, and validation.
- `src/calculator.py` — Shared electricity consumption and cost calculation functions.
- `src/electricity_prices.py` — Eurostat API integration.
- `tests/test_calculator.py` — Automated calculation tests.
- `test_main.py` — Test runner.
- `requirements.txt` — Project's Python package dependencies.
- `docs/tests.md` — Testing approach, examples, and results.
- `docs/diagrams/` — Activity and sequence diagrams for the CLI workflow and Eurostat interaction.
- `README.md` — Project overview, installation, usage, and limitations.

## Limitations

- Only three countries are supported for Eurostat price retrieval.
- Eurostat data is statistical reference data, not a live or personalized electricity tariff.
- Appliance data and dashboard settings are stored in memory/session state, not persistently saved.
- Monthly calculations assume 30 days; yearly calculations assume 365 days.
- Electricity consumption estimates assume constant appliance power during the entered usage hours. Actual consumption may vary due to thermostat cycles, standby operation, or different device modes.
- Fixed charges and personalized supplier tariff structures are not included.
- An internet connection is required to retrieve new Eurostat prices.
- Dashboard chart displays only the five highest-cost appliances; the complete list can be managed with **View All**.
- Automated tests currently focus on calculation functions and do not cover the Streamlit UI, API integration, or all interactive CLI operations.
- Some unusual input values and exceptional conditions may not be handled.

## Project Status

The **command-line application** and **Streamlit dashboard** have been implemented, including shared calculation logic, appliance management, a savings simulator, and Eurostat integration.

Completed project work includes:

- Electricity consumption and cost calculations.
- Multiple-appliance management and monthly summaries.
- Appliance rankings and comparisons in the CLI.
- Streamlit dashboard with cost chart, quick calculator, and savings simulation.
- Manual and Eurostat electricity prices.
- Common input validation and error handling.
- Four automated calculation tests and testing documentation.
- Activity and sequence diagrams.
- Incremental development using Git and GitHub.

The dashboard layout and main workflows have been reviewed manually. All four existing automated calculation tests passed in the latest local run. The project is in **final documentation and release preparation**, ahead of submission and presentation.
