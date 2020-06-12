import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("CAL")

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")




root.mainloop()
