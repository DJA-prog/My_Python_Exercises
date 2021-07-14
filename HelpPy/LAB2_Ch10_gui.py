from tkinter import *

root = Tk()
root.title("Lab 2")
root.geometry('805x450+10+10')
root.config(bg='#84BF04')

tex = Listbox(root, height=13, width=100)
tex.grid(row=1, column=0)

n = 0
for x in range(100):
    n = 10 ** x + n
    tex.insert(x, n)


button_exit = Button(root, text="Exit", width=8, pady=20, command=root.destroy)
button_exit.grid(row=0, column=0)
Label(root, text="Scrollable").grid(row=2, column=0)

root.mainloop()
