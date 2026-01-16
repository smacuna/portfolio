import csv
from datetime import datetime


def get_stock_prices() -> dict[str, dict[str, float]]:
    """
    Returns a dictionary of the stock prices, grouped by symbol and date.
    """
    stocks = dict()
    with open("data/stock_prices.csv", "r") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None or len(reader.fieldnames) <= 1:
            return stocks

        for row in reader:
            for symbol in reader.fieldnames[1:]:
                if symbol not in stocks:
                    stocks[symbol] = dict()

                # Obtener solo día, sin hora
                date = datetime.strptime(row["DATE"], "%d/%m/%Y %H:%M:%S").strftime(
                    "%d/%m/%Y"
                )
                stocks[symbol][date] = float(row[symbol].replace(",", "."))
    return stocks


def get_valid_dates() -> list[str]:
    """
    Returns a list of valid dates.
    """
    dates = []
    with open("data/stock_prices.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            date = datetime.strptime(row["DATE"], "%d/%m/%Y %H:%M:%S").strftime(
                "%d/%m/%Y"
            )

            dates.append(date)
    return dates


if __name__ == "__main__":
    print(get_stock_prices())
