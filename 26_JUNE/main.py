
# class chair:
#     def __init__(self, legs, backSupport, cushion):
#         self.legs = legs
#         self.backSupport = backSupport
#         self.cushion = cushion

# from module_001 import calc
#
# val1 = input("Value one: ")
# val2 = input("Value two: ")
# oper = input("Choose: '+' '-' '*' '/': ")
# calcs = calc(val1, val2)
#
# if oper == "+":
#     print(calcs.add())
#
# elif oper == "-":
#     print(calcs.sub())
#
# elif oper == "*":
#     print(calcs.multi())
#
# elif oper == "/":
#     print(calcs.div())
# else:
#     print(f"{oper} is not a choice of input!")
num = "+"
try:
    print(int(num))
except ValueError:
    print("not an int")