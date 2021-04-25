num1 = int(input("Put in a number: "))
num_str = str(num1)

if num1%2 == 0:
    s = "me "
    print(s+num_str)
else:
    print(f'{num1}')
