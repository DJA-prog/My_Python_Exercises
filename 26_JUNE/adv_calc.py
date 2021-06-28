from tkinter import *
from adv_calc_oper import *
import xml.etree.ElementTree as ET
from datetime import datetime

present_time = datetime.now()
xml_tree = ET.parse('history1.xml')  # parse xml file
xml_root = xml_tree.getroot()  # get root element

root = Tk()
root.title("Advanced calc")
root.geometry('331x273+10+20')
root.config(bg='#F6D55C')

screen0 = Entry(root)
screen0.grid(row=0, column=0, columnspan=4)
screen0.config(bg='#3CAEA3', fg="black", borderwidth=4, width=40)
screen1 = Entry(root)
screen1.grid(row=1, column=0, columnspan=4)
screen1.config(bg='#3CAEA3', fg="black", borderwidth=4, width=40)

screen_int = ""
screen_input = []
bedmas = ["^", ".inv", "/", "*", "+", "-"]
history_index = 0
history_index_max = 0

for child in xml_root:
    history_index_max += 1


def next_id():
    next_id_var = 0
    for child_id in xml_root:
        if next_id_var < int(child_id.attrib["id"]):
            next_id_var = int(child_id.attrib["id"])
    return next_id_var + 1


def button_click(number):
    global screen_int
    try:
        screen_int = screen1.get() + str(int(number))
        screen1.delete(0, END)
        screen1.insert(0, screen_int)
    except ValueError:
        global screen_input
        screen_input.append(screen_int)
        screen_input.append(number)
        screen0.delete(0, END)
        screen1.delete(0, END)
        disp = ""
        for each in screen_input:
            disp += str(each)
        screen0.insert(0, disp)
        print(screen_input)
        if number == ".inv":
            button_equal()


def button_history():
    global history_index
    global history_index_max
    print("max", history_index_max)
    screen0.delete(0, END)
    screen1.delete(0, END)
    xml_screen0 = str(xml_root[history_index].attrib["id"]) + " -- " + str(
        xml_root[history_index].attrib["date"]) + " -- " + str(xml_root[history_index].attrib["time"])
    screen0.insert(0, str(xml_screen0))
    xml_screen1 = str(xml_root[history_index].attrib["equation"]) + " = " + str(
        xml_root[history_index].attrib["answer"])
    screen1.insert(0, str(xml_screen1))
    history_index += 1
    if history_index == history_index_max:
        history_index = 0


def button_C_history():
    for child_id in xml_root:
        xml_root.remove(child_id)
    xml_tree.write('history1.xml')


def button_clear():
    global screen_input
    global history_index
    global screen_int
    screen0.delete(0, END)
    screen1.delete(0, END)
    screen_int = ""
    screen_input = []
    history_index = 0


def button_equal():
    global screen_input
    global screen_int
    global history_index_max
    screen_input.append(screen_int)
    screen0.delete(0, END)
    screen1.delete(0, END)
    disp = ""
    for each in screen_input:
        disp += str(each)
    screen0.insert(0, disp)
    answer = 0
    screen1.delete(0, END)
    for oper in bedmas:
        for input_index in screen_input:
            if input_index == oper:
                oper_index = screen_input.index(oper)
                if oper == "^":
                    calculate = Calcu(screen_input[oper_index - 1], screen_input[oper_index + 1])
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.power()
                elif oper == ".inv":
                    calculate = Calcu(screen_input[oper_index - 1], "0")
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.inverse()
                elif oper == "*":
                    calculate = Calcu(screen_input[oper_index - 1], screen_input[oper_index + 1])
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.multiplication()
                elif oper == "/":
                    calculate = Calcu(screen_input[oper_index - 1], screen_input[oper_index + 1])
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.division()
                elif oper == "+":
                    calculate = Calcu(screen_input[oper_index - 1], screen_input[oper_index + 1])
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.addition()
                elif oper == "-":
                    calculate = Calcu(screen_input[oper_index - 1], screen_input[oper_index + 1])
                    [screen_input.pop(oper_index) for a in range(2)]
                    screen_input[oper_index - 1] = calculate.subtraction()
    screen1.delete(0, END)
    screen1.insert(0, screen_input[0])
    history_index_max = 0
    new_data_id = next_id()
    data = ET.Element("calculation", {"id": str(new_data_id), "date": str(present_time.strftime('%d-%m-%Y')), "time": str(present_time.strftime('%H-%M-%S')), "equation": str(disp), "answer": str(answer)})
    xml_root.append(data)
    xml_tree.write('history1.xml')
    for x in xml_root:
        history_index_max += 1


Button(root, text="1", command=lambda: button_click(1), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=0)
Button(root, text="2", command=lambda: button_click(2), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=1)
Button(root, text="3", command=lambda: button_click(3), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=2)
Button(root, text="4", command=lambda: button_click(4), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=0)
Button(root, text="5", command=lambda: button_click(5), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=1)
Button(root, text="6", command=lambda: button_click(6), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=2)
Button(root, text="7", command=lambda: button_click(7), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=0)
Button(root, text="8", command=lambda: button_click(8), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=1)
Button(root, text="9", command=lambda: button_click(9), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=2)
Button(root, text="0", command=lambda: button_click(0), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=1)
Button(root, text="C", command=button_clear, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=0)
Button(root, text="=", command=button_equal, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=2)
Button(root, text="+", command=lambda: button_click("+"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=3)
Button(root, text="-", command=lambda: button_click("-"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=3)
Button(root, text="*", command=lambda: button_click("*"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=3)
Button(root, text="/", command=lambda: button_click("/"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=3)
Button(root, text="1/x", command=lambda: button_click(".inv"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=0)
Button(root, text="X^a", command=lambda: button_click("^"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=1)
Button(root, text="Hist.", command=button_history, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=2)
Button(root, text="C Hist.", command=button_C_history, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=3)

root.mainloop()
