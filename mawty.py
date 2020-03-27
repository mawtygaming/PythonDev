from tkinter import *

ui = Tk()
ui.title("Calculator")

numberBox = Entry(ui, width=35)
numberBox.grid(row=0, column=1, columnspan=3)

# numberBox.insert
def buttonClick(number):
    current = numberBox.get()
    numberBox.delete(0, END)
    numberBox.insert(0, str(current) + str(number))

def buttonErase():
    numberBox.delete(1, END)

def buttonAdd():
    firstNum = numberBox.get()
    global fNum
    global math
    math = "add"
    fNum = int(firstNum)
    numberBox.delete(0, END)

def buttonSub():
    firstNum = numberBox.get()
    global fNum
    global math
    math = "sub"
    fNum = int(firstNum)
    numberBox.delete(0, END)

def buttonMul():
    firstNum = numberBox.get()
    global fNum
    global math
    math = "mul"
    fNum = int(firstNum)
    numberBox.delete(0, END)

def buttonDiv():
    firstNum = numberBox.get()
    global fNum
    global math
    math = "div"
    fNum = int(firstNum)
    numberBox.delete(0, END)

def buttonEqual():
    secondNum = numberBox.get()
    numberBox.delete(0, END)

    if math == "add":
        numberBox.insert(0, fNum + int(secondNum))
    if math == "sub":
        numberBox.insert(0, fNum - int(secondNum))
    if math == "mul":
        numberBox.insert(0, fNum * int(secondNum))
    if math == "div":
        numberBox.insert(0, fNum / int(secondNum))


def buttonDelete():
    numberBox.delete(0, END)

btnOne = Button(ui, text = "1", pady=30, padx=30, command=lambda : buttonClick(1)).grid(row=1, column=1)
btnTwo = Button(ui, text = "2", pady=30, padx=30, command=lambda : buttonClick(2)).grid(row=1, column=2)
btnThree = Button(ui, text = "3", pady=30, padx=30, command=lambda : buttonClick(3)).grid(row=1, column=3)
btnFour = Button(ui, text = "4", pady=30, padx=30, command=lambda : buttonClick(4)).grid(row=2, column=1)
btnFive = Button(ui, text = "5", pady=30, padx=30, command=lambda : buttonClick(5)).grid(row=2, column=2)
btnSix = Button(ui, text = "6", pady=30, padx=30, command=lambda : buttonClick(6)).grid(row=2, column=3)
btnSeven = Button(ui, text = "7", pady=30, padx=30, command=lambda : buttonClick(7)).grid(row=3, column=1)
btnEight = Button(ui, text = "8", pady=30, padx=30, command=lambda : buttonClick(8)).grid(row=3, column=2)
btnNine = Button(ui, text = "9", pady=30, padx=30, command=lambda : buttonClick(9)).grid(row=3, column=3)
btnZero = Button(ui, text = "0", pady=30, padx=30, command=lambda : buttonClick(0)).grid(row=4, column=1)
btnAdd = Button(ui, text = "+", pady=30, padx=30, command=buttonAdd).grid(row=4, column=2)
btnMinus = Button(ui, text = "-", pady=30, padx=30, command=buttonSub).grid(row=4, column=3)
btnMul = Button(ui, text = "x", pady=30, padx=30, command=buttonMul).grid(row=5, column=1)
btnDiv = Button(ui, text = "/", pady=30, padx=31, command=buttonDiv).grid(row=5, column=2)
btnEqual = Button(ui, text = "=", pady=30, padx=30, command=buttonEqual).grid(row=5, column=3)
btnErase = Button(ui, text = "<--", pady=30, padx=25,command=lambda : buttonErase()).grid(row=6, column=3)
btnClear = Button(ui,text = "CLEAR", pady=30, padx=60, command=lambda : buttonDelete()).grid(row=6, column=1, columnspan=2)

ui.mainloop()