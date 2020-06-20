#!/usr/bin/python

from tkinter import *
import math
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Simple Calculator")
root.resizable(0,0) ## Disable maximize button
## set window icon
root.iconphoto(False, PhotoImage(file='/home/rajib/PYTHON-programme/gui-tkinter/calculator-project/icon-calculator.png')) 
#root.geometry("360x370")

e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

## Create ation of function button_click()
reset = "not equal"
def button_click(number):
    global reset
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    if reset == "equal":
        e.delete(0, END)
        e.insert(0, str(number))
        reset = "not equal"

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    if first_number == "":
        first_number = 0
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    if first_number == "":
        first_number = 0
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()
    if first_number == "":
        first_number = 0
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    if first_number == "":
        first_number = 0
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_sqroot():
    first_number = e.get()
    #print(first_number)
    if first_number == "":
        first_number = 0
    e.delete(0, END)
    f_num1 = float(first_number)
    res = f_num1 ** 0.5
    e.insert(0, res)
    #first_number = 0

def button_x_power_y():
    first_number = e.get()
    if first_number == "":
        first_number = 0
    global f_num
    global math
    f_num = float(first_number)
    e.delete(0, END)
    math = "power"

def button_equal():
    global reset
    reset = "equal"
    second_number = e.get()
    if second_number == "":
        second_number = 0
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtract":
        e.insert(0, f_num - float(second_number))
    if math == "multiply":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "power":
        e.insert(0, f_num ** float(second_number))

#Create buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_point = Button(root, text=".", padx=30, pady=20, command=lambda: button_click("."))
button_sqroot = Button(root, text='\u221A', padx=30, pady=20, command=button_sqroot)
button_clear = Button(root, text="C", padx=20, pady=20, command=button_clear)
button_add = Button(root, text="+", padx=20, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_multiplication = Button(root, text="x", padx=20, pady=20, command=button_multiplication)
button_divide = Button(root, text="\u00f7", padx=20, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal)
button_power = Button(root, text="x\u207f", padx=20, pady=20, command=button_x_power_y)
#button_quit = Button(root, text="Exit", padx=20, pady=20, command=root.quit)

#Put the button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_point.grid(row=4, column=1)
button_sqroot.grid(row=4, column=2)
button_add.grid(row=1, column=4)
button_subtract.grid(row=1, column=5)
button_multiplication.grid(row=2, column=4)
button_divide.grid(row=2, column=5)
button_clear.grid(row=3, column=4)
button_equal.grid(row=3, column=5)
button_power.grid(row=4, column=3, columnspan=2)
#button_quit.grid(row=4, column=3, columnspan=3)








root.mainloop()
