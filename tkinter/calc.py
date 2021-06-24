from tkinter import *

root = Tk() # First lines(basic window)
root.title("Simple calc")

entry = Entry(root, width=35, fg="black", borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    entry.delete(0, END)

def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multi():
    first_number = entry.get()
    global f_num
    global math
    math = "multi"
    f_num = int(first_number)
    entry.delete(0, END)

def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if (math == "add"):
        entry.insert(0, f_num + int(second_number))
    elif (math == "sub"):
        entry.insert(0, f_num - int(second_number))
    elif (math == "multi"):
        entry.insert(0, f_num * int(second_number))
    else:
        entry.insert(0, f_num / int(second_number))

button_1 = Button(root, text="1", width=8, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=8, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=8, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=8, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=8, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=8, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=8, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=8, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=8, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=8, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", width=8, pady=20, command=button_add)
button_sub = Button(root, text="-", width=8, pady=20, command=button_sub)
button_multi = Button(root, text="*", width=8, pady=20, command=button_multi)
button_div = Button(root, text="/", width=8, pady=20, command=button_div)
button_clear = Button(root, text="Clear", width=8, pady=20, command=button_clear)
button_equal = Button(root, text="=", width=8, pady=20, command=button_equal)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_multi.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)


root.mainloop()#event loop
