from yahoo_fin import stock_info as si
import yfinance as yf

StockShares = ['DOW','YELP','AAPL', 'GME', 'MSFT', 'ELVT', 'ATVI', 'JNJ', 'TSLA']

def main():
    for ticker in StockShares:
        openPrice = (yf.Ticker(ticker)).info['open']
        livePrice = si.get_live_price(ticker)
        change = livePrice - openPrice
        print(ticker + " @ " + str(round(livePrice,2)) + (" up $" if change > 0 else " down $") + str(abs(round(change,2))),end='\r')


main()
