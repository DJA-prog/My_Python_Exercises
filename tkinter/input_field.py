from tkinter import *

root = Tk() # First lines(basic window)

entry = Entry(root, width=50, fg="black", bg="green", borderwidth=6)
entry.pack()
# entry.get()
entry.insert(0, "Name here")

def myClick():
    hello = "Hello: " + entry.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

# mybutton = Button(root, text="Click me here!", command=myClick, fg="blue", bg="green")
mybutton = Button(root, text="Click me here!", command=myClick, fg="blue", bg="green")
mybutton.pack()

#event loop
root.mainloop()
