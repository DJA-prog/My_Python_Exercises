import os

def cls():
   os.system('cls' if os.name=='nt' else 'clear')

bidders = {}
cont = ''

while (cont != "no"):
    name = input("Your name: ").title()
    cash_amount = int(input("Bidding amount: N$ "))
    bidders[name] = cash_amount
    cont = input("Is there any other bidders? [NO] or [YES]: ").lower()
    cls()

high_bid = 0
for bidder in bidders:
    if (bidders[bidder] > high_bid):
        high_bid = bidders[bidder]
        sold_to = bidder

print(f"Item sold to {sold_to} for N$ {bidders[sold_to]}")
