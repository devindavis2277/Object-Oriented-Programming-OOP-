# if-statement was used to for the function
# definition function was also included
# class attributes and init method was used to run code

class Asset:
    def __init__(self, ticker, price, high, low, volume):
        self.ticker = ticker
        self.price = price
        self.high = high
        self.low = low
        self.volume = volume

    def basic_info(self):
        print(self.ticker)
        print(self.price)
        print(self.high)
        print(self.low)
        print(self.volume)

robinhoods = Asset('HOOD', 27.90, 33, 19.50, 8752240)

robinhoods.basic_info()

class Stock(Asset):
    def __init__(self, ticker, price, high, low, volume, open_p, close_p, earnings):
        super().__init__(ticker, price, high, low, volume)
        self.open_p = open_p
        self.close_p = close_p
        self.earnings = earnings
        self.rate_return = (close_p / open_p) - 1

    def update(self, open_p, close_p):
        self.open_p = open_p
        self.close_p = close_p
        self.rate_return = (close_p / open_p) - 1

    def print_return(self):
        print(self.rate_return)

    def p_e_ratio(self):
        if self.earnings != 0:
            pe_ratio = self.close_p / self.earnings
            print(f"{pe_ratio:.2f}")

    def info(self):
        self.basic_info()
        print(self.open_p)
        print(self.close_p)
        print(self.earnings)

robinhoods2 = Stock('HOOD', 27.06, 33, 19.50, 8752240, 27.50, 28.08, 0.12)
robinhoods2.info()
robinhoods2.print_return()
robinhoods2.p_e_ratio()


robinhoods2.update(26.92, 27.75)
robinhoods2.print_return()

# 3
class Asset:
    def __init__(self, ticker, price, high, low, volume):
        self.ticker = ticker
        self.price = price
        self.high = high
        self.low = low
        self.volume = volume

    def info(self):
        print(self.ticker)
        print(self.price)
        print(self.high)
        print(self.low)
        print(self.volume)

class Crypto(Asset):
    def __init__(self, ticker, price, high, low, volume, circulating_supply):
        super().__init__(ticker, price, high, low, volume)
        self.circulating_supply = circulating_supply

    def info(self):
        super().info()
        print(self.circulating_supply)

crypto_asset = Crypto("BTC", 21548.59, 22534.78, 19879.34, 11700000000, 19100000)
crypto_asset.info()

