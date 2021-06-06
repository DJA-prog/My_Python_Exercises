items = {} #dictionary for items
def add_item(item, price, discount):
    items[item] = [price, str(round(discount, 2))]

discount_percent = int(input("Discount percent (number only): "))
item = input("Item: ").split(',')
price = input("Item price (number only): ").split(',')

for z in range(len(item)):
    discount = int(price[z]) - (int(price[z]) * discount_percent/100)
    add_item(item[z], price[z], discount)

for x in items:
    print(f"{x} : ${items[x][1].rjust(7)}")
