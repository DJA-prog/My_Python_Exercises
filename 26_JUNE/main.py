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
# num = "+"
# try:
#     print(int(num))
# except ValueError:
#     print("not an int")

import xml.etree.ElementTree as ET
from datetime import datetime

present_time = datetime.now()

tree = ET.parse('history.xml')  # parse xml file
root = tree.getroot()  # get root element
# print(root.tag)
# print(root.attrib)

print(present_time.strftime('%d-%m-%Y'))
print(present_time.strftime('%H-%M-%S'))


def next_id():
    next_id_var = 0
    for child_id in root:
        if next_id_var < int(child_id.attrib["id"]):
            next_id_var = int(child_id.attrib["id"])
    return next_id_var + 1


next_id_var_end = next_id()
equation = "28/2"
answer = 14


def new_entry():
    new_element = ET.SubElement(root, "calculation")
    root.append(new_element)
    root[next_id_var_end - 1].set("id", str(next_id_var_end))
    new_element_1 = ET.SubElement(root, "date")
    root[next_id_var_end - 1].append(new_element_1)
    root[next_id_var_end - 1][0].text = str(present_time.strftime('%d-%m-%Y'))
    new_element_2 = ET.SubElement(root, "time")
    root[next_id_var_end - 1].append(new_element_2)
    root[next_id_var_end - 1][1].text = str(present_time.strftime('%H-%M-%S'))
    new_element_3 = ET.SubElement(root, "equation")
    root[next_id_var_end - 1].append(new_element_3)
    root[next_id_var_end - 1][2].text = str(equation)
    new_element_4 = ET.SubElement(root, "answer")
    root[next_id_var_end - 1].append(new_element_4)
    root[next_id_var_end - 1][3].text = str(answer)
    tree.write('history1.xml')


new_entry()

# print("--", ET.SubElement(root, "calculation"))
# print("ID: ", root[0].attrib["id"])
# print("Date: ", root[0][0].text)
# print("Time: ", root[0][1].text)
# print("Equation: ", root[0][2].text)
# print("Answer: ", root[0][3].text)

for child in root:
    # print(child)
    # print(child.tag, child.attrib)
    print("ID: ", child.attrib["id"])
    print("Date: ", child[0].text)
    print("Time: ", child[1].text)
    print("Equation: ", child[2].text)
    print("Answer: ", child[3].text)
