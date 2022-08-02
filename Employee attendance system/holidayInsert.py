import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def holione():
    
    def holiInsert():
        if len(e1.get())==0:
            
            e1.config(bg='Red')
            e2.config(bg='Red')
            e3.config(bg='Red')
            
            messagebox.showwarning("Warning","please fill it all")

        elif len(e2.get())==0:
               e2.config(bg='Red')
               e3.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e3.get())==0:
               
               e3.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
      
        
        else:
        
            db = pymysql.connect(host='localhost', user='root',
                                 password='root', database='company')
            cur = db.cursor()
            a = e1.get()
            b = e2.get()
            c = e3.get()
            s = "insert into HMaster values('%s','%s','%s')" % (
                a, b, c)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Data saved", "Saved")
            e1.delete(0, 100)
            e2.delete(0, 100)
            e3.delete(0, 100)
            db.close()
            
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
           
            
    l1 = Label(c, text='HOLIDAY MASTER DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Holiday Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    e1 = Entry(c, width=50)
    e1.place(x=400, y=120, height=35)
    
    l3 = Label(c, text='Holiday Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=400, y=180, height=35)
    
    l4 = Label(c, text='Date Of Holiday :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=400, y=240, height=35)
    
    bt12 = Button(c, text='SAVE', width=40, height=1,font=('Times new roman',15),command=holiInsert)
    bt12.place(x=400, y=450)
    
    