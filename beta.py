#!/usr/bin/env python3
from tkinter import *

# class Layout:
    # Main:
calc = Tk()
calc.title("Calculette de merde")
calc.configure(background="orange")

# make buttons fit the window (column / row)
calc.grid_columnconfigure(0, weight=1)
calc.grid_columnconfigure(1, weight=1)
calc.grid_columnconfigure(2, weight=1)
calc.grid_columnconfigure(3, weight=1)

calc.grid_rowconfigure(0, weight=1)
calc.grid_rowconfigure(1, weight=1)
calc.grid_rowconfigure(2, weight=1)
calc.grid_rowconfigure(3, weight=1)
calc.grid_rowconfigure(4, weight=1)
calc.grid_rowconfigure(5, weight=1)
calc.grid_rowconfigure(6, weight=1)


def btnClick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)
    return

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEqual():
    global operator
    result = str(eval(operator))
    text_Input.set(result)
    operator = ""

operator = ""
text_Input = StringVar()

#create display
    
textDisplay = Entry(textvariable=text_Input, font=('arial', 18, 'bold'), justify='right')
textDisplay.grid(row=0, column=0, columnspan = 5, sticky=N+S+W+E)


#create button

#top line (sin cos tan surprise)
Button(calc, text="sin", command = lambda:btnClick('sin')) .grid(row=1, column=0, sticky=N+S+W+E)
Button(calc, text="cos", command = lambda:btnClick('cos')) .grid(row=1, column=1, sticky=N+S+W+E)
Button(calc, text="tan", command = lambda:btnClick('tan')) .grid(row=1, column=2, sticky=N+S+W+E)
Button(calc, text="²", command = lambda:btnClick('²')) .grid(row=1, column=3, sticky=N+S+W+E)

# top middle line (c / * <-)
Button(calc, text="C", command = lambda:btnClear()) .grid(row=2, column=0, sticky=N+S+W+E)
Button(calc, text="/", command = lambda:btnClick('/')) .grid(row=2, column=1, sticky=N+S+W+E)
Button(calc, text="*", command = lambda:btnClick('*')) .grid(row=2, column=2, sticky=N+S+W+E)
Button(calc, text="<-", command = lambda:btnClick('<-')) .grid(row=2, column=3, sticky=N+S+W+E)

# bottom middle line (7 8 9 -)
Button(calc, text="7", command = lambda:btnClick('7')) .grid(row=3, column=0, sticky=N+S+W+E)
Button(calc, text="8", command = lambda:btnClick('8')) .grid(row=3, column=1, sticky=N+S+W+E)
Button(calc, text="9", command = lambda:btnClick('9')) .grid(row=3, column=2, sticky=N+S+W+E)
Button(calc, text="-", command = lambda:btnClick('-')) .grid(row=3, column=3, sticky=N+S+W+E)


# bottom middle line (4 5 6 +)
Button(calc, text="4", command = lambda:btnClick('4')) .grid(row=4, column=0, sticky=N+S+W+E)
Button(calc, text="5", command = lambda:btnClick('5')) .grid(row=4, column=1, sticky=N+S+W+E)
Button(calc, text="6", command = lambda:btnClick('6')) .grid(row=4, column=2, sticky=N+S+W+E)
Button(calc, text="+", command = lambda:btnClick('+')) .grid(row=4, column=3, sticky=N+S+W+E)

# bottom middle line (1 2 3 =)
Button(calc, text="1", command = lambda:btnClick('1')) .grid(row=5, column=0, sticky=N+S+W+E)
Button(calc, text="2", command = lambda:btnClick('2')) .grid(row=5, column=1, sticky=N+S+W+E)
Button(calc, text="3", command = lambda:btnClick('3')) .grid(row=5, column=2, sticky=N+S+W+E)
Button(calc, text="=", command = lambda:btnEqual()) .grid(row=5, rowspan=2, column=3, sticky=N+S+W+E)

# bottom  line (surprise 0 , =)
Button(calc, text=":)", command = lambda:btnClick('I <3 Gecko')) .grid(row=6, column=0, sticky=N+S+W+E)
Button(calc, text="0", command = lambda:btnClick('0')) .grid(row=6, column=1, sticky=N+S+W+E)
Button(calc, text=",", command = lambda:btnClick('.')) .grid(row=6, column=2, sticky=N+S+W+E)



#rue the main loop
calc.mainloop()