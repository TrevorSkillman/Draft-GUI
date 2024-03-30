from tkinter import *
from players import *

window = Tk()

strvar = StringVar(window, "Hello ")
setint = IntVar(window, value=5)
# Setting values
window.setvar(name="str", value="QB")
window.setvar(name="int", value=52)
window.setvar(name="bool", value=False)

# Getting Values
print("Value of StringVar()", window.getvar(name="str"))
print("Value of IntVar())", window.getvar(name="int"))
print("Value of BooleanVar())", window.getvar(name="bool"))


