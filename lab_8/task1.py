from tkinter import *
from tkinter.messagebox import showerror
import math

root = Tk()
root.minsize(width=350, height=150)
root.maxsize(width=500, height=300)
root.title("Calculator")

# Change background and text
fr_xy = Frame(root, bg='lightblue', cursor='hand2')
fr_xy.pack(side=TOP, expand=YES, fill=X)

lx = Label(fr_xy, text="x =", bg='lightblue', fg='blue')
lx.pack(side=LEFT, padx=10, pady=10)
entX = Entry(fr_xy)
entX.insert(0, 0)
entX.pack(side=LEFT, padx=10, pady=10)
entX.focus()

ly = Label(fr_xy, text="y =", bg="lightblue", fg="blue")
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy)
entY.insert(0, 0)
entY.pack(side=LEFT, padx=10, pady=10)

fr_op = LabelFrame(root, text="Operation:", bg="lightgreen", cursor="hand2")
fr_op.pack(side=TOP, expand=YES, fill=X)

oper = ['+', '-', '*', '/', '%', '√x', 'y²']

varOper = StringVar()
for op in oper:
    Radiobutton(fr_op, text=op, variable=varOper, value=op, bg="lightgreen", fg="green").pack(side=LEFT, padx=20,
                                                                                              pady=10)

varOper.set(oper[0])

fr_res = Frame(root, bg="lightyellow", cursor="hand2")
fr_res.pack(side=TOP, expand=YES, fill=BOTH)


def OnButtonResult():
    try:
        x = float(entX.get())
    except ValueError:
        showerror("Fill error", "Variable x is not a number")
        return

    try:
        y = float(entY.get())
    except ValueError:
        showerror("Fill error", "Variable y is not a number")
        return

    op = varOper.get()
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y if y != 0 else 'NAN'
    elif op == '%':
        res = x % y if y != 0 else 'NAN'
    elif op == '√x':
        res = math.sqrt(x) if x >= 0 else 'NAN'
    elif op == 'y²':
        res = y ** 2
    else:
        res = 'Operation selected incorrectly'

    lres['text'] = res


Button(fr_res, text="=", width=10, command=OnButtonResult).pack(side=LEFT, padx=30, pady=20)
lres = Label(fr_res, text="", bg="lightyellow", fg="black")
lres.pack(side=LEFT, padx=30, pady=20)

root.mainloop()