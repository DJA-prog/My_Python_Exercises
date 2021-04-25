pizza_open = 'y'
allowed_size = ['s','m','l']
allowed_input = ['y','n']
while pizza_open == 'y':
    print("Welcome to DCS Pizza Deliveries! (Case matters not)")

    size = input("What size pizza would you like? S, M, or L: ") # S=50 M=80 L=100
    while allowed_size.count(size.lower()) == 0:
        size = input("We only make S, M, or L size pizza. Which would you like: ") # S=50 M=80 L=100

    pepperoni = input("Would you like some pepperoni? Y or N: ") # S=15 M&L=25
    while allowed_input.count(pepperoni.lower()) == 0:
        pepperoni = input("Was that a Y or N for pepperoni?: ") # S=15 M&L=25

    cheese = input("Would you like some extra cheese? Y or N: ") # S&M&L=15
    while allowed_input.count(cheese.lower()) == 0:
        cheese = input("Was that a Y or N for extra cheese?: ")# S&M&L=15

    bill = 0
    if size == 's':
        bill += 50
        if pepperoni == 'y':
            bill += 15
        if cheese  == 'y':
            bill += 15
    elif size == 'm':
        bill += 80
        if pepperoni == 'y':
            bill += 25
        if cheese  == 'y':
            bill += 15
    elif size == 'l':
        bill += 100
        if pepperoni == 'y':
            bill += 25
        if cheese  == 'y':
            bill += 15

    if bill == 0:
        print("Order failed due to incorrect size input")
    else:
        print(f"Your final Bill is {bill}")

    pizza_open = input("Is the still shop open: ") or 'y'
    while allowed_input.count(pizza_open.lower()) == 0:
        pizza_open = input("Is the still shop open: ") or 'y'

print("We are closed!")
