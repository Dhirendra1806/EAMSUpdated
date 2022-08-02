import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql

def workplanone():
    
    def workInsert():
        db = pymysql.connect(host='localhost', user='root',
                             password='root', database='company')
        cur = db.cursor()
        a = e1.get()
        b = x1.get()
        c = x2.get()
        d = x3.get()
        e = x4.get()
        f = x5.get()
        g = x6.get()
        h = x7.get()
        s = "insert into wplan values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            a, b, c, d, e, f, g, h)
        cur.execute(s)
        db.commit()
        messagebox.showinfo("Data saved", "Saved")
        e1.delete(0, 100)
        
        db.close()
    
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
   
    
    l1 = Label(c, text='WORK PLAN DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Plan Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    e1 = Entry(c, width=22, font=('Times new roman', 20))
    e1.place(x=350, y=120, height=30)
   
    
    l3 = Label(c, text='Sunday :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    x1=IntVar()
    cb1=Checkbutton(c,width=40,height=1,variable=x1,onvalue=1,offvalue=0)
    cb1.place(x=350,y=180)
    
    
    l4 = Label(c, text='Monday :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    x2=IntVar()
    cb2=Checkbutton(c,width=40,height=1,variable=x2,onvalue=1,offvalue=0)
    cb2.place(x=350,y=240)
    
    
    
    l4 = Label(c, text='Tuesday :', font=('Times new roman', 20))
    l4.place(x=120, y=300)
    x3=IntVar()
    cb3=Checkbutton(c,width=40,height=1,variable=x3,onvalue=1,offvalue=0)
    cb3.place(x=350,y=300)
    
    
    l5 = Label(c, text='Wednesday :', font=('Times new roman', 20))
    l5.place(x=120, y=360)
    x4=IntVar()
    cb4=Checkbutton(c,width=40,height=1,variable=x4,onvalue=1,offvalue=0)
    cb4.place(x=350,y=360)
    
    
    l6 = Label(c, text='Thursday :', font=('Times new roman', 20))
    l6.place(x=120, y=420)
    x5=IntVar()
    cb5=Checkbutton(c,width=40,height=1,variable=x5,onvalue=1,offvalue=0)
    cb5.place(x=350,y=420)
    
    
    l7 = Label(c, text='Friday :', font=('Times new roman', 20))
    l7.place(x=120, y=490)
    x6=IntVar()
    cb6=Checkbutton(c,width=40,height=1,variable=x6,onvalue=1,offvalue=0)
    cb6.place(x=350,y=490)
    
    
    l8 = Label(c, text='Saturday :', font=('Times new roman', 20))
    l8.place(x=120, y=550)
    x7=IntVar()
    cb7=Checkbutton(c,width=40,height=1,variable=x7,onvalue=1,offvalue=0)
    cb7.place(x=350,y=550)
    
    
    bt18 = Button(c, text='SAVE', width=40, height=1,font=('Times new roman',15),command=workInsert)
    bt18.place(x=500, y=600)
    
    