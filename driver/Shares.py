from yahoo_fin import stock_info as si

StockShares = ['DOW','YELP','AAPL', 'GME', 'MSFT', 'ELVT', 'ATVI', 'JNJ', 'TSLA']
change = 0
direction = "up"

def main():

    for ticker in StockShares:
        change = si.get_live_price(ticker) - si.get_postmarket_price(ticker)
        if (change > 0):
            direction = "up"
        else:
            direction = "down"
        change = str(round(change,2))
        print(ticker + " @ " + str(round(si.get_live_price(ticker), 2)) + " "+direction +" "+ change)

main()
