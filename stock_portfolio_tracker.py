# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found. Please enter a valid stock name.")

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock} - {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("\nDo you want to save the portfolio to a CSV file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.csv", "w") as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(f"{stock},{quantity},{stock_prices[stock]},{investment}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print("Portfolio saved successfully as portfolio.csv")
else:
    print("Portfolio not saved.")
