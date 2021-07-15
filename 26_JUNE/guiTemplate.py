from tkinter import *
from calculatorM import *

rootGUI = Tk()
rootGUI.title("Hello World")
rootGUI.geometry('360x240+20+20')  # Pixels (XxY+posX+posY)
rootGUI.config(bg="lime")

e0 = Entry(rootGUI)
e0.grid(row=0, column=0, columnspan=4)
e0.config(bg='#3CAEA3', fg="black", borderwidth=4, width=40)
e1 = Entry(rootGUI)
e1.grid(row=1, column=0, columnspan=4)
e1.config(bg='#3CAEA3', fg="black", borderwidth=4, width=40)

screen_int = ""
screen_input = []
bedmas = ["^", ".inv", "/", "*", "+", "-"]


def button_click(number):
    global screen_int
    try:
        screen_int = e1.get() + str(int(number))
        e1.delete(0, END)
        e1.insert(0, screen_int)
    except ValueError:
        global screen_input
        screen_input.append(screen_int)
        screen_input.append(number)
        e0.delete(0, END)
        e1.delete(0, END)
        disp = ""
        for each in screen_input:
            disp += str(each)
        e0.insert(0, disp)


def button_history():
    pass


def button_clear():
    e0.delete(0, END)
    e1.delete(0, END)
    global screen_input
    screen_input = ""


def button_equal():
    answer = 0
    e1.delete(0, END)
    for oper in bedmas:
        for input_index in screen_input:
            if input_index == oper:
                calculate = ""
                if oper == "^":
                    calculate = (screen_input.index(oper) - 1)
                    answer = calculate.invert()
                elif oper == ".inv":
                    calculate = (screen_input[screen_input.index(oper) - 1], screen_input[screen_input.index(oper) + 1])
                    answer = calculate.power()
                elif oper == "*":
                    calculate = (screen_input.index(oper) - 1, screen_input.index(oper) + 1)
                    answer = calculate.multiplication()
                elif oper == "/":
                    calculate = (screen_input.index(oper) - 1, screen_input.index(oper) + 1)
                    answer = calculate.division()
                elif oper == "+":
                    calculate = (screen_input.index(oper) - 1, screen_input.index(oper) + 1)
                    answer = calculate.addition()
                elif oper == "-":
                    calculate = (screen_input.index(oper) - 1, screen_input.index(oper) + 1)
                    answer = calculate.subtraction()
    e1.delete(0, END)
    e1.insert(0, answer)


Button(rootGUI, text="1", command=lambda: button_click(1), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=0)
Button(rootGUI, text="2", command=lambda: button_click(2), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=1)
Button(rootGUI, text="3", command=lambda: button_click(3), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=2)
Button(rootGUI, text="4", command=lambda: button_click(4), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=0)
Button(rootGUI, text="5", command=lambda: button_click(5), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=1)
Button(rootGUI, text="6", command=lambda: button_click(6), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=2)
Button(rootGUI, text="7", command=lambda: button_click(7), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=0)
Button(rootGUI, text="8", command=lambda: button_click(8), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=1)
Button(rootGUI, text="9", command=lambda: button_click(9), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=2)
Button(rootGUI, text="0", command=lambda: button_click(0), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=1)
Button(rootGUI, text="C", command=button_clear, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=0)
Button(rootGUI, text="=", command=button_equal, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=2)
Button(rootGUI, text="+", command=lambda: button_click("+"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=3)
Button(rootGUI, text="-", command=lambda: button_click("-"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=3)
Button(rootGUI, text="*", command=lambda: button_click("*"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=3)
Button(rootGUI, text="/", command=lambda: button_click("/"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=3)
Button(rootGUI, text="1/x", command=lambda: button_click(".inv"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=0)
Button(rootGUI, text="X^a", command=lambda: button_click("^"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=6, column=1)
Button(rootGUI, text="History", command=button_history, bg='#173F5F', fg="#ED553B", padx=53, pady=10).grid(row=6, column=2, columnspan=2)

rootGUI.mainloop()