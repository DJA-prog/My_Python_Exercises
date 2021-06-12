evens = 0
for x in range(1, 101):
    if (x%2 == 0):
        evens += x
print(f"Sumation of even numbers from 1 to 100 is {evens}")

evens = 0
for z in range(0, 101, 2):
    evens += z
print(f"Sumation of even numbers from 1 to 100 is {evens}")
