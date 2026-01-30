print("Welcome to Stock Price Viewer")

stock = input("Enter stock name (example: AAPL): ")

# Sample stock prices (mock data)
stock_data = {
    "AAPL": 175.32,
    "TSLA": 248.56,
    "GOOGL": 142.11,
    "MSFT": 387.20
}

if stock in stock_data:
    print("Fetching data...")
    print("Current price of", stock, "is:", stock_data[stock])
else:
    print("Stock not found. Please try again.")