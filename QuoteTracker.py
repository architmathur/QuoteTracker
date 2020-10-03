import yfinance as yf

def getQuote(tickerSymbol):


	tickerData = yf.Ticker(tickerSymbol)

	print(tickerData.info['shortName'])

	print(tickerData.info['website'])

tck = input("Enter the ticker: ")
getQuote(tck)






