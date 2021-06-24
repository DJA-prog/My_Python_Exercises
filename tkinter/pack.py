from tkinter import *

root = Tk() # First lines(basic window)

#label Widget
mylabel = Label(root, text="Hello World!") #define / create widget
mylabel.pack()#print #pack , just places in window, not organised

#event loop
root.mainloop()
