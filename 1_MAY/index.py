# Do not forget to use the random module
import random
#Don't change the code below
seed_number = int(input("Create your seed number: "))
random.seed(seed_number)

#Split the string
names_as_csv = input("Give everybody's names(separated by , and space): ")
names = names_as_csv.split(", ")
#Don't change the code above

#Your codes goes below this line
name_length = len(names)
customer_pay = names[random.randint(0, name_length-1)]
print(f"{customer_pay} should pay the bill.")
