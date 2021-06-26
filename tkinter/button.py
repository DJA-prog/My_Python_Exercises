from tkinter import *

root = Tk() # First lines(basic window)

def myClick():
    mylabel=Label(root, text="Hi there")
    mylabel.pack()

#button Widget
# mybutton = Button(root, text="Click me here!", state=DISABLED)
# mybutton = Button(root, text="Click me here!", padx=50, pady=50)
mybutton = Button(root, text="Click me here!", command=myClick, fg="blue", bg="green") #can use hex colors
mybutton.pack()

#event loop
root.mainloop()
