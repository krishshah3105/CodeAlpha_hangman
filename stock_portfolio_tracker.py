"""Stock Portfolio Tracker

User enters stock symbols and quantities, and the script calculates total investment value
using a hardcoded price dictionary. Optionally saves results to a text or CSV file.
"""

import csv
import os

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 130,
    "AMZN": 150,
}


def get_stock_input():
    print("Enter stock purchases in the format SYMBOL quantity.")
    print("Type 'done' when finished. Example: AAPL 5")

    portfolio = {}
    while True:
        entry = input("Stock entry: ").strip()
        if not entry:
            continue
        if entry.lower() == "done":
            break

        parts = entry.split()
        if len(parts) != 2:
            print("Invalid format. Use SYMBOL quantity. For example: AAPL 5")
            continue

        symbol, qty_str = parts[0].upper(), parts[1]
        if not qty_str.isdigit():
            print("Quantity must be a positive integer.")
            continue

        quantity = int(qty_str)
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    return portfolio


def calculate_total_value(portfolio):
    total = 0
    details = []
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES.get(symbol)
        if price is None:
            details.append((symbol, quantity, None, None))
            continue

        value = price * quantity
        details.append((symbol, quantity, price, value))
        total += value

    return details, total


def print_portfolio(details, total):
    print("\nStock Portfolio Summary")
    print("-----------------------------------")
    print(f{"Symbol":<8} {"Qty":<6} {"Price":<8} {"Value":<10}")
    print("-----------------------------------")
    for symbol, qty, price, value in details:
        if price is None:
            print(f"{symbol:<8} {qty:<6} {'N/A':<8} {'N/A':<10}")
        else:
            print(f"{symbol:<8} {qty:<6} ${price:<7} ${value:<9}")
    print("-----------------------------------")
    print(f"Total investment value: ${total}")


def save_results(details, total, filename):
    basename, ext = os.path.splitext(filename)
    if ext.lower() == ".csv":
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for symbol, qty, price, value in details:
                writer.writerow([
                    symbol,
                    qty,
                    price if price is not None else "N/A",
                    value if value is not None else "N/A",
                ])
            writer.writerow([])
            writer.writerow(["Total", "", "", total])
    else:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-----------------------------------\n")
            file.write(f"{'Symbol':<8} {'Qty':<6} {'Price':<8} {'Value':<10}\n")
            file.write("-----------------------------------\n")
            for symbol, qty, price, value in details:
                if price is None:
                    file.write(f"{symbol:<8} {qty:<6} {'N/A':<8} {'N/A':<10}\n")
                else:
                    file.write(f"{symbol:<8} {qty:<6} ${price:<7} ${value:<9}\n")
            file.write("-----------------------------------\n")
            file.write(f"Total investment value: ${total}\n")


def main():
    print("Stock Portfolio Tracker")
    print("Hardcoded prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")

    portfolio = get_stock_input()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    details, total = calculate_total_value(portfolio)
    print_portfolio(details, total)

    save_choice = input("Do you want to save the summary to a file? (yes/no): ").strip().lower()
    if save_choice in {"yes", "y"}:
        filename = input("Enter filename (example: portfolio.txt or portfolio.csv): ").strip()
        if filename:
            save_results(details, total, filename)
            print(f"Results saved to {filename}")
        else:
            print("No filename entered. Summary not saved.")


if __name__ == "__main__":
    main()
