from tkinter import *
from calculatorM import *

root = Tk()
root.title("Advanced calc")
root.geometry('331x245+10+20')
root.config(bg='#F6D55C')

screen = Entry(root)
screen.grid(row=0, column=0, columnspan=4)
screen.config(bg='#3CAEA3', fg="black", borderwidth=4, width=40)
screen_input = ""


def button_click(number):
    global screen_input
    screen_input = screen.get() + str(number)
    screen.delete(0, END)
    screen.insert(0, screen_input)


def button_history():
    pass


def button_clear():
    screen.delete(0, END)
    global screen_input
    screen_input = ""


def button_equal():
    global screen_input
    screen_input = screen.get()
    screen.delete(0, END)




Button(root, text="1", command=lambda: button_click(1), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=0)
Button(root, text="2", command=lambda: button_click(2), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=1)
Button(root, text="3", command=lambda: button_click(3), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=2)
Button(root, text="4", command=lambda: button_click(4), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=0)
Button(root, text="5", command=lambda: button_click(5), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=1)
Button(root, text="6", command=lambda: button_click(6), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=2)
Button(root, text="7", command=lambda: button_click(7), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=1, column=0)
Button(root, text="8", command=lambda: button_click(8), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=1, column=1)
Button(root, text="9", command=lambda: button_click(9), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=1, column=2)
Button(root, text="0", command=lambda: button_click(0), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=1)
Button(root, text="C", command=button_clear, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=0)
Button(root, text="=", command=button_equal, bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=2)
Button(root, text="+", command=lambda: button_click("+"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=1, column=3)
Button(root, text="-", command=lambda: button_click("-"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=2, column=3)
Button(root, text="*", command=lambda: button_click("*"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=3, column=3)
Button(root, text="/", command=lambda: button_click("/"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=4, column=3)
Button(root, text="1/x", command=lambda: button_click(".inv"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=0)
Button(root, text="X^a", command=lambda: button_click("^"), bg='#173F5F', fg="#ED553B", width=6, pady=10).grid(row=5, column=1)
Button(root, text="History", command=button_history, bg='#173F5F', fg="#ED553B", padx=53, pady=10).grid(row=5, column=2, columnspan=2)

root.mainloop()