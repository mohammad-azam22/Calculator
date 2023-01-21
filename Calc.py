#!/usr/bin/env python
# coding: utf-8

# In[52]:


from tkinter import *
import ast
from math import factorial
from math import pi
from math import e

# for sharp display of tkinter window
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


# In[57]:


# making window for calc
root = Tk()
root.title('My Calculator')
root.configure(bg='#4284f5')
root.geometry('600x800')
root.minsize(width=300, height=500)
root.maxsize(width=600, height=800)

# The Entry Widget is a Tkinter Widget used to Enter or display a single line of text. 
display = Entry(root)
display.grid(row=1, columnspan=6, pady=10, padx=10, ipadx=900,ipady=30)
display.config(font=('consolas 40 bold'), state='normal')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(5, weight=1)



#Code to add buttons to the Calculator
# row 1
Button(root,text=' 1 ',font='consolas 20', command = lambda: get_variables(1)).grid(row=2, column=0, sticky=N+E+W+S, ipady=20, ipadx=20, padx=(10,0))
Button(root,text=' 2 ',font='consolas 20', command = lambda: get_variables(2)).grid(row=2, column=1, sticky=N+E+W+S, ipady=20, ipadx=20)
Button(root,text=' 3 ',font='consolas 20', command = lambda: get_variables(3)).grid(row=2, column=2, sticky=N+E+W+S, ipady=20, ipadx=20)

# row 2
Button(root,text=' 4 ',font='consolas 20', command = lambda: get_variables(4)).grid(row=3, column=0, sticky=N+E+W+S, ipady=20, ipadx=20, padx=(10,0))
Button(root,text=' 5 ',font='consolas 20', command = lambda: get_variables(5)).grid(row=3, column=1, sticky=N+E+W+S, ipady=20, ipadx=20)
Button(root,text=' 6 ',font='consolas 20', command = lambda: get_variables(6)).grid(row=3, column=2, sticky=N+E+W+S, ipady=20, ipadx=20)

# row 3
Button(root,text=' 7 ',font='consolas 20', command = lambda: get_variables(7)).grid(row=4, column=0, sticky=N+E+W+S, ipady=20, ipadx=20, padx=(10,0))
Button(root,text=' 8 ',font='consolas 20', command = lambda: get_variables(8)).grid(row=4, column=1, sticky=N+E+W+S, ipady=20, ipadx=20)
Button(root,text=' 9 ',font='consolas 20', command = lambda: get_variables(9)).grid(row=4, column=2, sticky=N+E+W+S, ipady=20, ipadx=20)



#adding other buttons to the calculator
# row 4
Button(root,text="AC",font='consolas 20',command=lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(10,0))
Button(root,text=" 0 ",font='consolas 20',command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W, ipady=20, ipadx=20)
Button(root,text=" . ",font='consolas 20',command=lambda :get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W, ipady=20, ipadx=20)



Button(root,text=" + ",font='consolas 20',command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+E+W+S, ipady=20, ipadx=20)
Button(root,text=" - ",font='consolas 20',command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W, ipady=20, ipadx=20)
Button(root,text=" * ",font='consolas 20',command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W, ipady=20, ipadx=20)
Button(root,text=" / ",font='consolas 20',command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W, ipady=20, ipadx=20)



# adding new operations
Button(root,text=" π ",font='consolas 20',command= lambda :get_operation("π")).grid(row=2,column=4, sticky=N+E+W+S, ipady=20, ipadx=20)
Button(root,text="exp",font='consolas 20',command= lambda :get_operation("^")).grid(row=3,column=4, sticky=N+S+E+W, ipady=20, ipadx=20)
Button(root,text=" ( ",font='consolas 20',command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W, ipady=20, ipadx=20)
Button(root,text="^3",font='consolas 20',command= lambda :get_operation("^3")).grid(row=5,column=4, sticky=N+S+E+W, ipady=20, ipadx=20)



Button(root,text="<-",font='consolas 20',command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(0,10))
Button(root,text="e",font='consolas 20', command= lambda: get_operation('e')).grid(row=3,column=5, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(0,10))
Button(root,text=" ) ",font='consolas 20',command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(0,10))
Button(root,text="^2",font='consolas 20',command= lambda :get_operation("^2")).grid(row=5,column=5, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(0,10))
Button(root,text=" = ",font='consolas 20',command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W, ipady=20, ipadx=20, padx=(10,10), pady=(0,10))


# function to display numbers
def get_variables(num):
    display.insert(END,num)
      
# function to display basic_operators
def get_operation(operator):
    display.insert(END,operator)

basic_operators = ["+", "-", "*", "/"]
alphas = set(map(chr,range(65,123))) - set(map(chr,range(91,97)))

# equals (=) button function
def calculate():
    entire_string = display.get()
    flag = True
    for i in range(len(entire_string)-1):
        x = entire_string[i]
        y = entire_string[i+1]
        if x in basic_operators and y in basic_operators:
            clear_all()
            display.insert(0,'Invalid Syntax')
            display.config(state='disabled')
            flag = False
            break
    if 'π' in entire_string:
        entire_string = entire_string.replace("π", "pi")
    if '%' in entire_string:
        entire_string = entire_string.replace("%", "/100")
    if '^' in entire_string:
        entire_string = entire_string.replace("^", "**")
    if flag:
        clear_all()
        try:
            result = str(eval(entire_string))
            if len(result) > 12:
                result = "{:e}".format(float(result))
            display.insert(0,result)
        except:
            clear_all()
            display.insert(0,'Invalid Syntax')
            display.config(state='disabled')

# UNDO function
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)

# AC function        
def clear_all():
    display.config(state='normal')
    display.delete(0,END)

root.mainloop()


# In[ ]:




