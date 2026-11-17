
"""Retrieve electricity prices from Eurostat."""

import requests

URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_204"


def get_electricity_price(country_code: str) -> tuple[float | None, str | None]:
    """Get the latest available household electricity price."""

    params = {
        "geo": country_code,
        "freq": "S",
        "siec": "E7000",
        "nrg_cons": "KWH2500-4999",
        "unit": "KWH",
        "tax": "I_TAX",
        "currency": "EUR",
        "lastTimePeriod": 4
    }

    response = requests.get(URL, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    periods = data["dimension"]["time"]["category"]["index"]
    values = data["value"]

    for period, index in sorted(
        periods.items(), key=lambda item: item[1], reverse=True
    ):
        price = values.get(str(index))

        if price is not None:
            return float(price), period

    return None, None


if __name__ == "__main__":
    price, period = get_electricity_price("FR")

    if price is not None:
        print(f"Electricity price: {price:.4f} EUR/kWh")
        print(f"Data period: {period}")
    else:
        print("No electricity price available.")
