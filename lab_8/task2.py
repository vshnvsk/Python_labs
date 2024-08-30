from tkinter import *
from tkinter.messagebox import showerror, showinfo
import math

root = Tk()
root.title("Quadratic equation")
root.geometry("400x200")

frame_input = Frame(root)
frame_input.pack(pady=20)

Label(frame_input, text="a:").grid(row=0, column=0, padx=10)
entry_a = Entry(frame_input)
entry_a.grid(row=0, column=1)

Label(frame_input, text="b:").grid(row=1, column=0, padx=10)
entry_b = Entry(frame_input)
entry_b.grid(row=1, column=1)

Label(frame_input, text="c:").grid(row=2, column=0, padx=10)
entry_c = Entry(frame_input)
entry_c.grid(row=2, column=1)


def calculate_roots():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        showerror("Error", "Please enter correct numeric values.")
        return

    discriminant = b**2 - 4*a*c
    if a == 0:
        showerror("Error", "The coefficient a cannot be zero.")
        return

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        result = f"Two real roots: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2 * a)
        result = f"One real root: x = {x:.2f}"
    else:
        result = "No valid roots"

    showinfo("Result", result)


Button(root, text="Calculate", command=calculate_roots).pack(pady=20)

root.mainloop()