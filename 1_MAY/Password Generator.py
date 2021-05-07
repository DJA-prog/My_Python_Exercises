import random
import string
pass_list = []
PyPassword = ""

print("Welcome to the NUST DSC PyPassword Generator!!!")
letter_count = int(input("How many letters would you like in your password?: "))
symbol_count = int(input("How many symbols would you like in your password?: "))
number_count = int(input("How many numbers would you like in your password?: "))

#letters_pass = random.randint(0, 9)

for letters_in_pass in range(letter_count):
    pass_list.append(random.choice(string.ascii_letters))

for symbols_in_pass in range(symbol_count):
    pass_list.append(random.choice(string.punctuation))

for numbers_in_pass in range(number_count):
    pass_list.append(random.randint(0, 9))

random.shuffle(pass_list)
for x in pass_list:
    x = str(x)
    PyPassword += x

print(f"Your Generated Password: {PyPassword}")
