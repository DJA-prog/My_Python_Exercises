# imports
import module_1
import random

# module_1
print(f"PI = {module_1.pi}\n")

# random
random_int = random.randint(1, 20)
print(f"Random integer = {random_int}\n")

random_int = random.random()
print(f"Random float = {random_int}\n")

random_int = random.random()*5
print(f"Random float integer = {random_int}\n")

#random.seed(23)
random_int = random.random()*5
print(f"Random seed = {random_int}\n")

list_01 = ["fruits", "flowers", "vegtables", "books", "cities", "countries", "history"]
list_01_length = len(list_01)
list_01_which = random.randint(0, list_01_length-1)
list_01_subject = list_01[list_01_which]
print(f"I love to study about {list_01_subject}")

list_01.append("animals")

list_01_length = len(list_01)
for x in range(list_01_length):
    list_01_subject = list_01[x]
    print(f"I love to study about {list_01_subject}")
print("#############")
list_01_length = len(list_01)
for x in range(list_01_length):
    list_01_subject = list_01[-x]
    print(f"I love to study about {list_01_subject

varin = "Here we go again"
