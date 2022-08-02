import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql

def amstwo():
    
    def finddata():
        db = pymysql.connect(host='localhost', user='root',
                             password='root', database='company')
        cur=db.cursor()
        x=a.get()
        s="select ename,date,status from ams where empid= '%s' "%(x)
        cur.execute(s)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])  
        e4.insert(0,data[2])
        db.close()
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select empid from ams" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def atmUpdate():
        if len(e1.get())==0:
            
            e1.config(bg='Red')
            e2.config(bg='Red')
            e3.config(bg='Red')
            e4.config(bg='Red')
            messagebox.showwarning("Warning","please fill it all")
    
        elif len(e2.get())==0:
               e2.config(bg='Red')
               e3.config(bg='Red')
               e4.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e3.get())==0:
               
               e3.config(bg='Red')
               e4.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e4.get())==0:
               e4.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        else:
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='company')
            cur=db.cursor()
            b=e2.get()
            c=e3.get()
            d=e4.get()
            
            x=a.get()
                
            s="update ams set ename='%s',date of mark='%s',status='%s' where empid='%s'"%(b,c,d,x)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Update","Updated..")
            a.delete(0,100)
            db.close()
            
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
        
    
    l1 = Label(c, text='ATTENDANCE MASTER DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Employee Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    a=ttk.Combobox(c, width=50)
    a.place(x=400,y=120, height=30)
    data=filldata()
    a['values']=data
    #e1 = Entry(t, width=50)
    #e1.place(x=400, y=120, height=35)
    
    l3 = Label(c, text='Employee Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=400, y=180, height=35)
    
    l4 = Label(c, text='Date Of Mark :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=400, y=240, height=35)
    
    
    l4 = Label(c, text='Status :', font=('Times new roman', 20))
    l4.place(x=120, y=300)
    e4 = Entry(c, width=50)
    e4.place(x=400, y=300, height=35)
    
    bt22 = Button(c, text='UPDATE', width=40, height=1,font=('Times new roman',15),command=atmUpdate)
    bt22.place(x=400, y=450)
    bt23 = Button(c, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
    bt23.place(x=400, y=550)
    
    