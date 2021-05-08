import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-','|','/', ':','@']
pass_list = []
PyPassword = ""

print("Welcome to the NUST DSC PyPassword Generator!!!")
letter_count = int(input("How many letters would you like in your password?: "))
symbol_count = int(input("How many symbols would you like in your password?: "))
number_count = int(input("How many numbers would you like in your password?: "))

#letters_pass = random.randint(0, 9)

for letters_in_pass in range(letter_count):
    pass_list.append(random.choice(letters))

for symbols_in_pass in range(symbol_count):
    pass_list.append(random.choice(symbols))

for numbers_in_pass in range(number_count):
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)

for x in pass_list:
    x = str(x)
    PyPassword += x

print(f"Your Generated Password: {PyPassword}")
