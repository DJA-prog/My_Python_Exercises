# Do not forget to ues the random module
import random

# Don't change the code below
seed_number = int(input("Create your seed number: "))
random.seed(seed_number)

# Split the string
name_as_csv = input("Give everybody's names (separated by , and space):  ")
names = name_as_csv.slipt(", ")
# Don't change the code above

# Your code goes below this line
names_len = len(names)
names_pay = names[random.randint(0, names_len-1)]
print(f"{names_pay} will pay the bill.")
