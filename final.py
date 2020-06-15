import sympy

import tkinter
from tkinter import *
from tkinter import messagebox

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("400x590")
root.resizable(0, 0)
root.title("Calculator")


global li
li = []
global ip
ip = 0
global count
count = 0
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


def btn_dot_isclicked():
    global val
    val = val + "."
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_mult_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_c_pressed():
    global A, operator, val, ip
    val = ""
    A = 0
    ip = 0
    operator = ""
    data.set(val)
    datar.set(val)
    
def btn_ce_isclicked():
    global A, operator, val, ip	
    val = ""	
    A = 0	
    ip = 0	
    operator = ""	
    data.set(val)	
    datar.set(val)

# function to find the result
def result():
    global A, operator, val, val2
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        datar.set(val)
    if operator == "-":
        x = float((val2.split("-")[1]))
        C = A - x
        val = str(C)
        datar.set(val)
    if operator == "*":
        x = float((val2.split("*")[1]))
        C = A * x
        val = str(C)
        datar.set(val)
    if operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            datar.set(val)
        else:
            C = float(A / x)
            datar.set(C)


def btnsave_clicked():
    global count
    li.append(val+"="+val2)
    print(li)
    count = count+1
    print(count)


def btnup_clicked():
    global ip
    if ip < 0 or ip >= count:
        ip = 0
        data.set(li[ip])
    else:
        data.set(li[ip])
        ip = ip+1


def btndown_clicked():
    global ip
    if ip < 0 or ip >= count:
        ip = 0
        data.set(li[ip])
    else:
        data.set(li[ip])
        ip = ip+1

def btn_bs_isclicked():
    global val
    val =(val[:-1])
    data.set(val)
    
def btn_x2_isclicked():	
    global val	
    val =str(pow(float(val), 2)) 	
    datar.set(val)	
    
def btn_sqrroot_isclicked():	
    global val	
    val =str(math.sqrt(float(val)))	
    datar.set(val)    
    


# the label that shows the result
data = StringVar()

datar = StringVar()


lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    height=2,
    textvariable=datar,
    background="#c8c8c8",
    fg="#000000",
)
lbl.pack(expand=True, fill="both")

lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    height=2,
    textvariable=data,
    background="#c8c8c8",
    fg="#000000",
)
lbl.pack(expand=True, fill="both")

# the frames section
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both", padx=10, pady=5)

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btnrow5 = Frame(root)
btnrow5.pack(expand=True, fill="both")

btnrow6 = Frame(root)
btnrow6.pack(expand=True, fill="both")

btnrow7 = Frame(root)
btnrow7.pack(expand=True, fill="both")

btnrow8 = Frame(root)
btnrow8.pack(expand=True, fill="both")


# The buttons section
# button for frame4
# btnc = Button(
#     btnrow4,
#     text="C",
#     font=("Verdana", 22),
#     highlightthickness=6,
#     activebackground='grey',
#     height=1,
#     width=1,
#     command=btn_c_pressed,
# )
# btnc.pack(side=LEFT, expand=True, fill="both",)

# btnsave = Button(
#     btnrow5,
#     text="save",
#     font=("Verdana", 22),
#     highlightthickness=6,
#     height=1,
#     width=1,
#     activebackground='grey',
#     command=btnsave_clicked,
# )
# btnsave.pack(side=LEFT, expand=True, fill="both",)

# btnup = Button(
#     btnrow5,
#     text="<",
#     font=("Verdana", 22),
#     highlightthickness=6,
#     height=1,
#     width=1,
#     activebackground='grey',
#     command=btnup_clicked,
# )
# btnup.pack(side=LEFT, expand=True, fill="both",)

# btndown = Button(
#     btnrow5,
#     text=">",
#     font=("Verdana", 22),
#     highlightthickness=6,
#     height=1,
#     width=1,
#     activebackground='grey',
#     command=btndown_clicked,
# )
# btndown.pack(side=LEFT, expand=True, fill="both",)

# layout change

# 7th row

btnmc = Button(
    btnrow1,
    text="MC",
    state=DISABLED,
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    activebackground='grey',
    height=1,
    width=1,
    # command=btn_7_isclicked,
)
btnmc.pack(side=LEFT, expand=True, fill="both",)

btnmr = Button(
    btnrow1,
    text="MR",
    state=DISABLED,
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    # command=btn_8_isclicked,
)
btnmr.pack(side=LEFT, expand=True, fill="both",)

btnmplus = Button(
    btnrow1,
    text=" M+ ",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    # command=btn_9_isclicked,
)
btnmplus.pack(side=LEFT, expand=True, fill="both",)

btnmminus = Button(
    btnrow1,
    text="M-",
    bg="#dddddd",
    font=("Verdana", 22),
    relief=FLAT,
    highlightthickness=6,
    height=1,
    width=1,
    # command=btn_div_clicked,
)
btnmminus.pack(side=LEFT, expand=True, fill="both",)

btnms = Button(
    btnrow1,
    text="MS",
    bg="#dddddd",
    font=("Verdana", 22),
    relief=FLAT,
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_div_clicked,
)
btnms.pack(side=LEFT, expand=True, fill="both",)

btnmps = Button(
    btnrow1,
    text="M'",
    state=DISABLED,
    bg="#dddddd",
    font=("Verdana", 22),
    relief=FLAT,
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_div_clicked,
)
btnmps.pack(side=LEFT, expand=True, fill="both",)


# 6th row

btnpercent = Button(
    btnrow2,
    text="%",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    activebackground='grey',
    height=1,
    width=1,
    # command=btn_7_isclicked,
)
btnpercent.pack(side=LEFT, expand=True, fill="both",)

btnsqrroot = Button(
    btnrow2,
    text="√",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_sqrroot_isclicked,,
)
btnsqrroot.pack(side=LEFT, expand=True, fill="both",)

# global f
# f = X**2
btnsqr = Button(
    btnrow2,
    text="x2",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_x2_isclicked,
)
btnsqr.pack(side=LEFT, expand=True, fill="both",)

btn1byx = Button(
    btnrow2,
    text="1/x",
    bg="#dddddd",
    font=("Verdana", 22),
    relief=FLAT,
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_ce_isclicked,
)
btn1byx.pack(side=LEFT, expand=True, fill="both",)

# 5th row

btnce = Button(
    btnrow3,
    text="CE",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    activebackground='grey',
    height=1,
    width=1,
    # command=btn_7_isclicked,
)
btnce.pack(side=LEFT, expand=True, fill="both",)

btnc = Button(
    btnrow3,
    text="C",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_c_pressed,
)
btnc.pack(side=LEFT, expand=True, fill="both",)

btnbs = Button(
    btnrow3,
    text=" ⌫ ",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_bs_isclicked,
)
btnbs.pack(side=LEFT, expand=True, fill="both",)

btndiv = Button(
    btnrow3,
    text="÷",
    bg="#dddddd",
    font=("Verdana", 22),
    relief=FLAT,
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_div_clicked,
)
btndiv.pack(side=LEFT, expand=True, fill="both",)

# 4th row

btn7 = Button(
    btnrow4,
    text="7",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    activebackground='grey',
    height=1,
    width=1,
    command=btn_7_isclicked,
)
btn7.pack(side=LEFT, expand=True, fill="both",)


def on_enter7(e):
    btn7['background'] = '#C0C0C0'


def on_leave7(e):
    btn7['background'] = 'SystemButtonFace'


btn7.bind("<Enter>", on_enter7)
btn7.bind("<Leave>", on_leave7)

btn8 = Button(
    btnrow4,
    text="8",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_8_isclicked,
)
btn8.pack(side=LEFT, expand=True, fill="both",)


def on_enter8(e):
    btn8['background'] = '#C0C0C0'


def on_leave8(e):
    btn8['background'] = 'SystemButtonFace'


btn8.bind("<Enter>", on_enter8)
btn8.bind("<Leave>", on_leave8)

btn9 = Button(
    btnrow4,
    text="9",
    activebackground='grey',
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_9_isclicked,
)
btn9.pack(side=LEFT, expand=True, fill="both",)


def on_enter9(e):
    btn9['background'] = '#C0C0C0'


def on_leave9(e):
    btn9['background'] = 'SystemButtonFace'


btn9.bind("<Enter>", on_enter9)
btn9.bind("<Leave>", on_leave9)

btnmult = Button(
    btnrow4,
    text="*",
    bg="#dddddd",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_mult_clicked,
)
btnmult.pack(side=LEFT, expand=True, fill="both",)

# 3rd row

btn4 = Button(
    btnrow5,
    text="4",
    activebackground='grey',
    relief=FLAT,
    font=("Verdana", 22),
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_4_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)


def on_enter4(e):
    btn4['background'] = '#C0C0C0'


def on_leave4(e):
    btn4['background'] = 'SystemButtonFace'


btn4.bind("<Enter>", on_enter4)
btn4.bind("<Leave>", on_leave4)

btn5 = Button(
    btnrow5,
    text="5",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    activebackground='grey',
    height=1,
    width=1,
    command=btn_5_isclicked,
)
btn5.pack(side=LEFT, expand=True, fill="both",)


def on_enter5(e):
    btn5['background'] = '#C0C0C0'


def on_leave5(e):
    btn5['background'] = 'SystemButtonFace'


btn5.bind("<Enter>", on_enter5)
btn5.bind("<Leave>", on_leave5)

btn6 = Button(
    btnrow5,
    text="6",
    activebackground='grey',
    relief=FLAT,
    font=("Verdana", 22),
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_6_isclicked,
)
btn6.pack(side=LEFT, expand=True, fill="both",)


def on_enter6(e):
    btn6['background'] = '#C0C0C0'


def on_leave6(e):
    btn6['background'] = 'SystemButtonFace'


btn6.bind("<Enter>", on_enter6)
btn6.bind("<Leave>", on_leave6)

btnminus = Button(
    btnrow5,
    text=" - ",
    relief=FLAT,
    bg="#dddddd",
    font=("Verdana", 22),
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_minus_clicked,
)
btnminus.pack(side=LEFT, expand=True, fill="both",)

# 2nd row

btn1 = Button(
    btnrow6,
    text="1",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    activebackground='grey',
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)


def on_enter1(e):
    btn1['background'] = '#C0C0C0'


def on_leave1(e):
    btn1['background'] = 'SystemButtonFace'


btn1.bind("<Enter>", on_enter1)
btn1.bind("<Leave>", on_leave1)

btn2 = Button(
    btnrow6,
    text="2",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    activebackground='grey',
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


def on_enter2(e):
    btn2['background'] = '#C0C0C0'


def on_leave2(e):
    btn2['background'] = 'SystemButtonFace'


btn2.bind("<Enter>", on_enter2)
btn2.bind("<Leave>", on_leave2)

btn3 = Button(
    btnrow6,
    text="3",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    activebackground='grey',
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)


def on_enter3(e):
    btn3['background'] = '#C0C0C0'


def on_leave3(e):
    btn3['background'] = 'SystemButtonFace'


btn3.bind("<Enter>", on_enter3)
btn3.bind("<Leave>", on_leave3)

btnplus = Button(
    btnrow6,
    text="+",
    font=("Verdana", 22),
    bg="#dddddd",
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=btn_plus_clicked,
)
btnplus.pack(side=LEFT, expand=True, fill="both",)

# 1st row bottom row

btnplusorminus = Button(
    btnrow7,
    text="±",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    activebackground='grey',
    # command=btn_1_isclicked,
)
btnplusorminus.pack(side=LEFT, expand=True, fill="both",)

btn0 = Button(
    btnrow7,
    text="0",
    font=("Verdana", 22),
    relief=FLAT,
    activebackground='grey',
    highlightthickness=6,
    height=1,
    width=1,
    command=btn_0_isclicked,
)
btn0.pack(side=LEFT, expand=True, fill="both",)


def on_enter0(e):
    btn0['background'] = '#C0C0C0'


def on_leave0(e):
    btn0['background'] = 'SystemButtonFace'


btn0.bind("<Enter>", on_enter0)
btn0.bind("<Leave>", on_leave0)

btndot = Button(
    btnrow7,
    text=".",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    activebackground='grey',
    command=btn_dot_isclicked,
)
btndot.pack(side=LEFT, expand=True, fill="both",)

btnequal = Button(
    btnrow7,
    text="=",
    font=("Verdana", 22),
    highlightthickness=6,
    relief=FLAT,
    height=1,
    width=1,
    command=result,
)
btnequal.pack(side=LEFT, expand=True, fill="both",)

root.mainloop()
