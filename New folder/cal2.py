
import tkinter
from tkinter import *
from tkinter import messagebox

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

val = ""
A = 0
operator = ""

# function for numerical button clicked

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)


# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)


# the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both" )

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
btn1 = Button(
    btnrow1,
    
    text = "1",
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
          activebackground='grey',
    
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)
def on_enter1(e):
    btn1['background'] = '#C0C0C0'

def on_leave1(e):
    btn1['background'] = 'SystemButtonFace'

btn1.bind("<Enter>", on_enter1)
btn1.bind("<Leave>", on_leave1)


btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
     activebackground='grey',
    
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)
def on_enter2(e):
    btn2['background'] = '#C0C0C0'

def on_leave2(e):
    btn2['background'] = 'SystemButtonFace'
    
btn2.bind("<Enter>", on_enter2)
btn2.bind("<Leave>", on_leave2)


btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
           activebackground='grey',
    
    
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)
def on_enter3(e):
    btn3['background'] = '#C0C0C0'

def on_leave3(e):
    btn3['background'] = 'SystemButtonFace'
    
btn3.bind("<Enter>", on_enter3)
btn3.bind("<Leave>", on_leave3)
btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    bg="orange",
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
          

    command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
     activebackground='grey',
    
    
    font = ("Verdana", 22),
   highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)
def on_enter4(e):
    btn4['background'] = '#C0C0C0'

def on_leave4(e):
    btn4['background'] = 'SystemButtonFace'
    
btn4.bind("<Enter>", on_enter4)
btn4.bind("<Leave>", on_leave4)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    highlightthickness=6,
     activebackground='grey',
    
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)
def on_enter5(e):
    btn5['background'] = '#C0C0C0'

def on_leave5(e):
    btn5['background'] = 'SystemButtonFace'
    
btn5.bind("<Enter>", on_enter5)
btn5.bind("<Leave>", on_leave5)

btn6 = Button(
    btnrow2,
    text = "6",
     activebackground='grey',
    
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

def on_enter6(e):
    btn6['background'] = '#C0C0C0'

def on_leave6(e):
    btn6['background'] = 'SystemButtonFace'
    
btn6.bind("<Enter>", on_enter6)
btn6.bind("<Leave>", on_leave6)

btnminus = Button(
    btnrow2,
    text = " - ",
     bg="orange",
    font = ("Verdana", 22),
   highlightthickness=6,
    relief=tkinter.SOLID,
     height = 1, 
          width = 1,
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
     activebackground='grey',
    
      height = 1, 
          width = 1,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)
def on_enter7(e):
    btn7['background'] = '#C0C0C0'

def on_leave7(e):
    btn7['background'] = 'SystemButtonFace'
    
btn7.bind("<Enter>", on_enter7)
btn7.bind("<Leave>", on_leave7)

btn8 = Button(
    btnrow3,
    text = "8",
     activebackground='grey',
    
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)
def on_enter8(e):
    btn8['background'] = '#C0C0C0'

def on_leave8(e):
    btn8['background'] = 'SystemButtonFace'
    
btn8.bind("<Enter>", on_enter8)
btn8.bind("<Leave>", on_leave8)

btn9 = Button(
    btnrow3,
    text = "9",
     activebackground='grey',
    
    font = ("Verdana", 22),
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)
def on_enter9(e):
    btn9['background'] = '#C0C0C0'

def on_leave9(e):
    btn9['background'] = 'SystemButtonFace'
    
btn9.bind("<Enter>", on_enter9)
btn9.bind("<Leave>", on_leave9)

btnmult = Button(
    btnrow3,
    text = "*",
     bg="orange",
    font = ("Verdana", 22),
     highlightthickness=6,
    relief=tkinter.SOLID,
     height = 1, 
          width = 1,
   
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
     highlightthickness=6,
    relief=tkinter.SOLID,
     activebackground='grey',
    
    height = 1, 
          width = 1,
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
     activebackground='grey',
    
    highlightthickness=6,
    relief=tkinter.SOLID,
      height = 1, 
          width = 1,
    
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)
def on_enter0(e):
    btn0['background'] = '#C0C0C0'

def on_leave0(e):
    btn0['background'] = 'SystemButtonFace'
    
btn0.bind("<Enter>", on_enter0)
btn0.bind("<Leave>", on_leave0)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
     highlightthickness=6,
    relief=tkinter.SOLID,
    
    
     height = 1, 
          width = 1,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
     bg="orange",
    font = ("Verdana", 22),
     highlightthickness=6,
    relief=tkinter.SOLID,
     height = 1, 
          width = 1,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()
