from services.stock_prices_service import get_valid_dates, get_stock_prices

current_stock_prices = get_stock_prices()
valid_dates = get_valid_dates()


class Stock:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def current_price(self, date: str) -> float:
        """
        Returns the current price of the stock on the given date.
        """
        if self.symbol not in current_stock_prices:
            raise ValueError("Stock not found")

        return current_stock_prices[self.symbol][date]


class PortfolioStock:
    def __init__(self, stock: Stock, quantity: float) -> None:
        self.stock = stock
        self.quantity = quantity

    def current_value(self, date: str) -> float:
        """
        Returns the current value of the stock on the given date.
        """
        return self.quantity * self.stock.current_price(date)

    def __repr__(self) -> str:
        return f"{self.stock.symbol}: {self.quantity}"


class Portfolio:
    def __init__(
        self, name: str, total_value: float, allocated_stocks: dict[str, float]
    ) -> None:
        self.name = name
        self.total_value = total_value
        self.stocks: dict[str, PortfolioStock] = dict()
        self.allocated_stocks: dict[str, float] = allocated_stocks

    @property
    def current_value(self, date: str) -> float:
        """
        Returns the total value of the portfolio on the given date.
        """
        sum: float = 0

        for stock in self.stocks.values():
            sum += stock.current_value(date)

        return sum

    def rebalance(self, date: str) -> None:
        """
        Rebalances the portfolio to the allocated stocks.
        """

        # Calcular el valor total objetivo de cada stock
        target_stock_values: dict[str, float] = dict()
        for symbol, percentage in self.allocated_stocks.items():

            stock = self.stocks.get(symbol)
            if stock is None:
                self.stocks[symbol] = PortfolioStock(Stock(symbol), 0)

            target_stock_values[symbol] = percentage * self.total_value

        # Comprar o vender stocks para alcanzar el valor objetivo
        for symbol, stock in self.stocks.items():
            stock_current_price = stock.stock.current_price(date)
            stock_current_value = stock.current_value(date)

            if stock_current_value < target_stock_values[symbol]:
                self.buy_stock(
                    symbol,
                    (target_stock_values[symbol] - stock_current_value)
                    / stock_current_price,
                )
            elif stock_current_value > target_stock_values[symbol]:
                self.sell_stock(
                    symbol,
                    (stock_current_value - target_stock_values[symbol])
                    / stock_current_price,
                )

    def buy_stock(self, stock_symbol: str, quantity: float) -> None:
        """
        Buys a stock, given the stock symbol and quantity.
        """
        if stock_symbol not in self.stocks:
            self.stocks[stock_symbol] = PortfolioStock(Stock(stock_symbol), 0)

        self.stocks[stock_symbol].quantity += quantity

        with open("results/results.csv", "a") as f:
            f.write(f"{self.name},{date},Buy,{stock_symbol},{quantity}\n")

    def sell_stock(self, stock_symbol: str, quantity: float) -> None:
        """
        Sells a stock, given the stock symbol and quantity.
        """
        stock = self.stocks.get(stock_symbol)
        if stock is None:
            raise ValueError("Stock not found")

        if stock.quantity < quantity:
            raise ValueError(
                "Current stock quantity must be greater than the quantity to sell"
            )

        self.stocks[stock_symbol].quantity -= quantity

        with open("results/results.csv", "a") as f:
            f.write(f"{self.name},{date},Sell,{stock_symbol},{quantity}\n")

    def __repr__(self) -> str:
        return f"Portfolio {self.name}: {self.stocks}"


if __name__ == "__main__":
    with open("results/results.csv", "w") as f:
        f.write("Portfolio,Date,Action,Stock,Quantity\n")

    portfolio_a = Portfolio(
        "Portfolio A",
        total_value=1000,
        allocated_stocks={
            "META": 0.2,
            "AAPL": 0.2,
            "GOOGL": 0.2,
            "MSFT": 0.2,
            "NVDA": 0.2,
        },
    )

    portfolio_b = Portfolio(
        "Portfolio B",
        total_value=1000,
        allocated_stocks={
            "AAPL": 0.3,
            "GOOGL": 0.3,
            "MSFT": 0.1,
            "AMZN": 0.1,
            "NVDA": 0.1,
            "KO": 0.1,
        },
    )

    portfolio_c = Portfolio(
        "Portfolio C",
        total_value=2000,
        allocated_stocks={
            "AAPL": 0.3,
            "GOOGL": 0.3,
            "MSFT": 0.1,
            "AMZN": 0.1,
            "NVDA": 0.1,
            "KO": 0.1,
        },
    )

    for date in valid_dates:
        portfolio_a.rebalance(date)
        portfolio_b.rebalance(date)
        portfolio_c.rebalance(date)

    print(portfolio_a)
    print(portfolio_b)
    print(portfolio_c)
