import tkinter
from tkinter import *
from AdminLogin import *
from tkinter import ttk
import pymysql
from AdminLogin import *

t = tkinter.Tk()
t.geometry('1200x1200')
t.config(bg='light blue')

l1 = Label(t, text='EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM', font=('Lucida Handwriring', 30),
           fg='grey', bg='light yellow', width=50, height=2)
l1.place(x=150, y=50)
l2 = Label(t, text='LOGIN PAGE', font=('Lucida Sans Unicode', 20),
           fg='Black', bg='White', width=40, height=2)
l2.place(x=370, y=200)
l3 = Label(t, text='Select the type of login you would like to use',
           font=('Verdana', 20), fg='Black', bg='White', width=40, height=2)
l3.place(x=350, y=350)

    




x1=StringVar()
vlist = ['ADMIN', 'USER']
cb = ttk.Combobox(t, values=vlist,textvariable=x1, font=('Lucida Fax', 20), width=10, height=2)
cb.set('SELECT')
cb.place(x=600, y=550)

t.mainloop()
