# Internship Tasks - Python

# ---------------- TASK 2 ----------------
def stock_portfolio_tracker():
    prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 150, "MSFT": 320}
    total = 0
    print("Available stocks:", ", ".join(prices.keys()))
    n = int(input("Enter number of stocks: "))
    results = []
    for i in range(n):
        name = input("Stock name: ").upper()
        qty = int(input("Quantity: "))
        if name in prices:
            value = prices[name] * qty
            total += value
            results.append(f"{name},{qty},{prices[name]},{value}")
        else:
            print("Stock not found.")
    print("Total Investment:", total)
    with open("portfolio.csv","w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for r in results:
            f.write(r+"\n")
        f.write(f"Total,,,{total}\n")

# ---------------- TASK 3 ----------------
import re

def extract_emails():
    with open("input.txt","r") as f:
        text = f.read()
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    with open("emails.txt","w") as f:
        for e in emails:
            f.write(e+"\n")
    print("Emails extracted.")

# ---------------- TASK 4 ----------------
def chatbot():
    print("Simple Chatbot (type 'bye' to exit)")
    while True:
        msg = input("You: ").lower()
        if msg == "hello":
            print("Bot: Hi!")
        elif msg == "how are you":
            print("Bot: I'm fine, thanks!")
        elif msg == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

if __name__ == "__main__":
    while True:
        print("\n1. Stock Portfolio Tracker")
        print("2. Email Extractor")
        print("3. Basic Chatbot")
        print("4. Exit")
        ch = input("Choose: ")
        if ch=="1":
            stock_portfolio_tracker()
        elif ch=="2":
            extract_emails()
        elif ch=="3":
            chatbot()
        elif ch=="4":
            break
        else:
            print("Invalid choice")
