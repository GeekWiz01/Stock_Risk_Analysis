import pandas as pd

# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

def get_prices(file_name:str):
    df = pd.read_csv(file_name)
    df.set_index("Date", inplace=True)
    close_px = df['Adj Close']

    return close_px

def plot_stock(stock):
    plt.clf()

    mavg = stock.rolling(window=100).mean()

    # Adjusting the size of matplotlib
    mpl.rc('figure', figsize=(8, 7))
    mpl.__version__

    # Adjusting the style of matplotlib
    style.use('ggplot')

    stock.plot(label='STOCK TIMELINE')
    mavg.plot(label='MAVG')
    plt.legend()

    plt.show()

def plot_returns(stock):
    plt.clf()

    # # print avg percent change
    # print("Average annual growth rate: ", stock.pct_change().mean()*36500, "%")
    # print(stock.pct_change().head(20))

    rets = stock / stock.shift(1) - 1
    rets.plot(label='return')

    print("% daily change:", rets.mean()*100)
    print("STD: ", rets.std())

    plt.show()

def aapl(section:int):
    close_px_appl = get_prices("AAPL.csv")
    subset = 0          # DUMMY DATA

    plot_stock(close_px_appl)

    if section == 1:
        subset = close_px_appl[:'2004-09-21']

    elif section == 2:
        subset = close_px_appl['2004-09-21':]

    else:
        exit("Nothing to choose")

    plot_returns(subset)

def goog():
    close_px_goog = get_prices("GOOG.csv")

    plot_stock(close_px_goog)

    plot_returns(close_px_goog)

def msft(section:int):
    close_px_msft = get_prices("MSFT.csv")
    subset = 0          # DUMMY DATA

    plot_stock(close_px_msft)

    if section == 1:
        subset = close_px_msft[:'1994-02-07']

    elif section == 2:
        subset = close_px_msft['2002-01-16':'2009-12-24']

    elif section == 3:
        subset = close_px_msft['2009-12-24':]

    else:
        exit("Nothing to choose")

    plot_returns(subset)

def voo():
    close_px_voo = get_prices("VOO.csv")

    plot_stock(close_px_voo)
    plot_returns(close_px_voo)

def nas():
    close_px = get_prices("NASDAQ.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

def xlk():
    close_px = get_prices("XLK.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

def xlv():
    close_px = get_prices("XLV.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

def xle():
    close_px = get_prices("XLE.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

def arkk():
    close_px = get_prices("ARKK.csv")

    plot_stock(close_px)
    plot_returns(close_px)

def amcpx():
    close_px = get_prices("AMCPX.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

def smcwx():
    close_px = get_prices("SMCWX.csv")
    close_px = close_px["2003-10-07":]

    plot_stock(close_px)
    plot_returns(close_px)

nas()