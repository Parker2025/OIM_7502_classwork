import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb  # optional to set plot theme
import yfinance as yf
sb.set_theme()  # optional to set plot theme


DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        self.data = yf.download(self.symbol, self.start, self.end, interval='1d')
        self.data = pd.DataFrame(self.data)
        self.data.index = pd.to_datetime(self.data.index)
        self.calc_returns()
        
        return self.data
        pass

    def calc_returns(self):
        self.data["Change in Close from Yesterday"] = self.data["Close"].diff()
        self.data["Instant Return"] = (np.log(self.data["Close"]).diff().round(4))
        ###^ not sure about that one.
        pass

    def plot_return_dist(self):
        plt.hist(self.data["Instant Return"], bins=50, density=True, edgecolor='w');
        pass

    def plot_performance(self):
        self.data["Percent Change"] = self.data["Close"].diff() / self.data["Close"].diff() * 100
        # I couldn't figure out the percent change column formula
        plt.plot(self.data["Percent Change"])
        pass


def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol=["AAPL"])  # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()
###I wasn't able to get the plots to run successfully in an IDE
### I was able to get the plot graph to run in Jupyter, can't figure out why that is.

if __name__ == '__main__':
    main()
