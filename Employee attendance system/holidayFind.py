import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql

def holithree():
    

    def finddata():
        db = pymysql.connect(host='localhost', user='root',
                             password='root', database='company')
        cur=db.cursor()
        x=a.get()
        s="select hname,date from HMaster where hid = '%s' "%(x)
        cur.execute(s)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])  
        db.close()
        
    def cl():
        a.delete(0,100)
        b.delete(0,100)
        c.delete(0,100)
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select hid from HMaster" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
       
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
   
    
    l1 = Label(c, text='HOLIDAY MASTER DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Holiday Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    a=ttk.Combobox(c, width=50)
    a.place(x=400,y=120, height=30)
    data=filldata()
    a['values']=data
    
    l3 = Label(c, text='Holiday Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=400, y=180, height=35)
    
    l4 = Label(c, text='Date Of Holiday :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=400, y=240, height=35)
    
    bt17 = Button(c, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
    bt17.place(x=400, y=500)
    
   
