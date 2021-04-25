allowed_input = [9,12,16,32]
is_num1_allowed = 0
num1 = int(input("Insert any of the following numbers (9; 12 ;16 ;32): "))

while is_num1_allowed == 0:
    num1 = int(input("Try again(9; 12 ;16 ;32): "))
    is_num1_allowed = allowed_input.count(num1)
#end while
print(f"You chose {num1}")
