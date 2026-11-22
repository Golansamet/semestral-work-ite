# Testing Documentation

## 1. Testing Approach

The Electricity Consumption Calculator uses automated tests and manual testing to verify its functionality.

Automated tests are implemented using the `pytest` framework. They focus on the core electricity consumption and cost calculation functions.

The tests compare calculated results against expected values obtained from the electricity consumption formulas.

Manual testing is used to verify the command-line interface, appliance management, input validation, and Eurostat API integration.

## 2. Automated Tests

The automated tests are located in:

`tests/test_calculator.py`

All tests can be executed using:

```bash
python test_main.py
```

Four automated tests have been implemented.

| Test | Sample Input | Expected Output |
|---|---|---|
| Monthly consumption | 100 W, 5 hours/day, 30 days | 15 kWh |
| Monthly cost | 100 W, 5 hours/day, 30 days, price 0.30/kWh | 4.50 |
| Zero daily usage | 100 W, 0 hours/day, 30 days | 0 kWh |
| Yearly consumption | 1000 W, 2 hours/day, 365 days | 730 kWh |

### Test 1 — Monthly Consumption

A television consumes 100 W and operates for 5 hours daily.

Expected monthly consumption:

100 / 1000 × 5 × 30 = 15 kWh

The test verifies that the calculation function returns 15 kWh.

### Test 2 — Monthly Cost

Using the same television with a price of 0.30 per kWh:

15 × 0.30 = 4.50

The test verifies that the monthly electricity cost is calculated correctly.

### Test 3 — Zero Usage

An appliance operating for zero hours should consume zero electricity.

Expected result: 0 kWh.

This test checks a boundary case.

### Test 4 — Yearly Consumption

An appliance consumes 1000 W and operates for 2 hours daily over 365 days.

Expected yearly consumption:

1000 / 1000 × 2 × 365 = 730 kWh

The test verifies the calculation for a longer period.

## 3. Manual Testing

The following features have also been tested manually:

- Adding appliances and viewing the appliance list.
- Calculating monthly consumption and costs.
- Ranking appliances by monthly electricity cost.
- Comparing electricity costs between two appliances.
- Calculating potential savings by reducing usage hours.
- Retrieving electricity prices from Eurostat.
- Handling invalid appliance power and daily usage input.
- Handling invalid manual electricity price input.
- Rejecting daily usage above 24 hours.

### Example — Appliance Comparison

Two appliances were tested using a price of 0.30 per kWh:

| Appliance | Power | Hours/day | Monthly Cost |
|---|---:|---:|---:|
| TV | 100 W | 5 | 4.50 |
| Air Conditioner | 1500 W | 4 | 54.00 |

Expected monthly cost difference: 49.50.

The application returned the expected result.

### Example — Invalid Input

When the user entered `abc` instead of a numeric electricity price, the application displayed:

```text
Invalid price! Please enter a number.
```

The application returned to the main menu without crashing.

### Example — Eurostat API

During manual testing, the following data was retrieved:

- Country: Czech Republic
- Electricity price: 0.2884 EUR/kWh
- Reporting period: 2026-S1

The API integration returned a valid electricity price and displayed its reporting period.

## 4. Test Results

The four automated tests were executed successfully.

Result:

```text
4 passed
```

Manual testing confirmed the expected behavior for the scenarios described above.

## 5. Testing Limitations

- Automated tests currently focus on the core calculation functions.
- Eurostat API integration has been tested manually, but does not yet have automated tests.
- Not every possible input combination and error condition has been tested.
- API results depend on the availability of Eurostat data and an internet connection.

The current testing approach provides basic verification of the application's main calculations and selected user interactions.