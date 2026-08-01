# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200,
    "MSFT": 300
}

print("===== Stock Portfolio Tracker =====")

total_investment = 0

while True:
    stock = input("\nEnter Stock Name (AAPL, TSLA, GOOGLE, AMZN, MSFT): ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Investment in {stock}: ${investment}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value = ${total_investment}")

# Save result to a text file
file = open("portfolio.txt", "w")
file.write("Stock Portfolio Tracker\n")
file.write("-------------------------\n")
file.write(f"Total Investment Value = ${total_investment}")
file.close()

print("Result saved in portfolio.txt")
