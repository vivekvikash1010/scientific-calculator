from tkinter import *
import math
root = Tk()
root.title("simple calculator")

def power(a,b):
    return math.pow(a,b)
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_number)
    e.delete(0, END)
def button_sub():
    first_number = e.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_div():
    first_number = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(first_number)
    e.delete(0, END)
def button_mul():
    first_number = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_pow():
    first_number = e.get()
    global f_num
    global operation
    operation = "power"
    f_num = int(first_number)
    e.delete(0, END)
def button_sin():
    first_number = e.get()
    global f_num
    global operation
    operation = "sin"
    f_num = int(first_number)
    print(first_number,f_num)
    e.delete(0,END)


def button_cos():
    first_number = e.get()
    global f_num
    global operation
    operation = "cos"
    f_num = int(first_number)
    e.delete(0, END)


def button_tan():
    first_number = e.get()
    global f_num
    global operation
    operation = "tan"
    f_num = int(first_number)
    e.delete(0, END)


def button_log():
    first_number = e.get()
    global f_num
    global operation
    operation = "log"
    f_num = int(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    global f_num
    global operation
    operation = "sqrt"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if operation == "addition":
        e.insert(0,f_num + int(second_number))
    if operation == "subtraction":
        e.insert(0,f_num - int(second_number))
    if operation == "division":
        e.insert(0,f_num / int(second_number))
    if operation == "multiplication":
        e.insert(0,f_num * int(second_number))
    if operation == "power":
        p = pow(int(f_num), int(second_number))
        e.insert(0, str(p))
    if operation == "sin":
        e.insert(0, str(math.sin(f_num)))
    if operation == "cos":
        e.insert(0, str(math.cos(f_num)))
    if operation == "tan":
        e.insert(0, math.tan(f_num))
    if operation == "log":
        e.insert(0, math.log(f_num))
    if operation == "sqrt":
        e.insert(0, math.sqrt(f_num))


e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1), fg ="#1c6891", bg = "black")
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2), fg ="#1c6891", bg = "black")
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3), fg ="#1c6891", bg = "black")
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4), fg ="#1c6891", bg = "black")
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5), fg ="#1c6891", bg = "black")
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6), fg ="#1c6891", bg = "black")
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7), fg ="#1c6891", bg = "black")
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8), fg ="#1c6891", bg = "black")
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9), fg ="#1c6891", bg = "black")
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0), fg ="#1c6891", bg = "black")
button_a = Button(root, text = "+", padx = 40, pady = 20, command = button_add, fg ="#1c6891", bg = "black")
button_s = Button(root, text = "-", padx = 40, pady = 20, command = button_sub, fg ="#1c6891", bg = "black")
button_d = Button(root, text = "/", padx = 40, pady = 20, command = button_div, fg ="#1c6891", bg = "black")
button_m = Button(root, text = "*", padx = 40, pady = 20, command = button_mul, fg ="#1c6891", bg = "black")
button_sin = Button(root, text = "sin", padx = 40, pady = 20, command = button_sin, fg ="#1c6891", bg = "black")
button_cos = Button(root, text = "cos", padx = 40, pady = 20, command = button_cos, fg ="#1c6891", bg = "black")
button_tan = Button(root, text = "tan", padx = 40, pady = 20, command = button_tan, fg ="#1c6891", bg = "black")
button_log = Button(root, text = "log", padx = 40, pady = 20, command = button_log, fg ="#1c6891", bg = "black")
button_p = Button(root, text = "pow", padx = 40, pady = 20, command = button_pow, fg ="#1c6891", bg = "black")
button_sqrt = Button(root, text = "sqrt", padx = 40, pady = 20, command = button_sqrt, fg ="#1c6891", bg = "black")
button_ans = Button(root, text = "Ans", padx = 40, pady = 20, command = button_equal, fg ="#1c6891", bg = "black")
button_clear = Button(root, text= "Clear", padx = 40, pady = 20, command= button_clear, fg ="#1c6891", bg = "black")
#put bottons on screen

button_1.grid(row=1, column =2 )
button_2.grid(row=1 , column =3 )
button_3.grid(row=1 , column =4 )
button_4.grid(row=2 , column =2 )
button_5.grid(row= 2, column = 3)
button_6.grid(row= 2, column = 4)
button_7.grid(row= 3, column =2 )
button_8.grid(row= 3, column = 3)
button_9.grid(row= 3, column = 4)
button_0.grid(row= 4, column = 3)

button_a.grid(row=1, column = 5)
button_s.grid(row=2 , column = 5)
button_d.grid(row=3 , column = 5)
button_m.grid(row=4 , column = 5)
button_sin.grid(row=1 , column = 0)
button_cos.grid(row=1 , column =1 )
button_tan.grid(row= 2, column =0 )
button_log.grid(row= 2, column =1 )
button_p.grid(row= 3, column =0 )
button_sqrt.grid(row=3 , column = 1)
button_ans.grid(row= 4, column =0 )
button_clear.grid(row = 4, column =1 )


root.mainloop()