import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from AdminMain import *

import tkinter
from PIL import ImageTk,Image

def frontone():

    t = tkinter.Tk()
    t.geometry('1550x900')
    t.config(bg='light blue')
    
    def Ok():
        
        uname=e1.get()
        password=e2.get() 
        
        if(uname=="" and password==""):
            messagebox.showinfo("","Blank Not Allowed")
            
            
        elif(uname and password):
            db = pymysql.connect(host='localhost', user='root',
                                     password='root', database='company')
            cur = db.cursor()
                
            s = "Select pass from adlogin where user=%s ",(password,uname)
            cur.execute(s)
            messagebox.showinfo("info", "Login Successfull")
            data=cur.fetchone()
            if data:
                messagebox.showinfo("Info","Login Succssfull")
                c=Canvas(width=1550,height=900,bg='grey')
                c.place(x=0,y=0)
                    
                    
                l1=Label(c,text='Employee',font=('Times new roman',15))
                l1.place(x=50,y=20)
                b1=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=Empone)
                b1.place(x=30,y=50)
                b2=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=Emptwo)
                b2.place(x=30,y=80)
                b3=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=Empthree)
                b3.place(x=30,y=110)
                b4=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=Empfour)
                b4.place(x=30,y=140)
                            
                l2=Label(c,text='Department',font=('Times new roman',15))
                l2.place(x=50,y=180)
                b5=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=deptone)
                b5.place(x=30,y=210)
                b6=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=depttwo)
                b6.place(x=30,y=240)
                b7=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=deptthree)
                b7.place(x=30,y=270)
                b8=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=deptfour)
                b8.place(x=30,y=300)
                    
                l3=Label(c,text='Work Plan',font=('Times new roman',15))
                l3.place(x=50,y=340)
                b9=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=workplanone)
                b9.place(x=30,y=370)
                b10=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=workplantwo)
                b10.place(x=30,y=400)
                b11=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=workplanthree)
                b11.place(x=30,y=430)
                b12=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=workplanfour)
                b12.place(x=30,y=460)
                            
                l4=Label(c,text='Holiday Master',font=('Times new roman',15))
                l4.place(x=40,y=500)
                b13=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11))
                b13.place(x=30,y=530)
                b14=Button(c,width=20,height=1,text='Update',font=('Times new roman',11))
                b14.place(x=30,y=560)
                b15=Button(c,width=20,height=1,text='find',font=('Times new roman',11))
                b15.place(x=30,y=590)
                b16=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11))
                b16.place(x=30,y=620)
                            
                l5=Label(c,text='Attendance Master',font=('Times new roman',15))
                l5.place(x=240,y=20)
                b17=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=amsone)
                b17.place(x=210,y=50)
                b18=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=amstwo)
                b18.place(x=210,y=80)
                b19=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=amsthree)
                b19.place(x=210,y=110)
                b20=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=amsfour)
                b20.place(x=210,y=140)
        
                    
                c.mainloop()
        
            else:
                messagebox.showerror("Info","Login failed")
            db.commit()
            db.close()
        
            
                
            
                  
        
                        
                        
                        
    '''            
    def RegInt():
                    db = pymysql.connect(host='localhost', user='root',
                                         password='root', database='company')
                    cur = db.cursor()
                    b=e6.get()
                    c=e7.get()
                    d=e8.get()
                    e=e9.get()
                    
                    x=a.get()
                    
                    s="insert into Register values('%s','%s','%s','%s')"%(b,c,d,e,x)
                    cur.execute(s)
                    db.commit()
                    messagebox.showinfo("Data Register", "Registered") 
                    e5.delete(0, 100)
                    e6.delete(0, 100) 
                    e7.delete(0, 100) 
                    e8.delete(0, 100)
                    e9.delete(0, 100)
                    
                    db.close()
                 
    def Register():
                    t = tkinter.Tk() 
                    t.geometry('1000x1000')
                    t.config(bg='light blue')
                
                    x = IntVar()
                
                    def change():
                        a = x.get()
                        if a == 0:
                            t.config(text='Male')
                        if a == 1:
                            t.config(text='Female')
                        if a == 2:
                            t.config(text='Others')
                
                    l6 = Label(t, text='ADMIN REGISTRATION', font=('Lucida Handwriting', 20),
                               fg='grey', bg='light yellow', width=50, height=1)
                    l6.place(x=250, y=50)
                    l7 = Label(t, text='Enter Name :', font=('Times New Roman', 20))
                    l7.place(x=120, y=120)
                    e5 = Entry(t, width=50)
                    e5.place(x=350, y=120, height=35)
                
                    l8 = Label(t, text='Enter Email :', font=('Times New Roman', 20))
                    l8.place(x=120, y=180)
                    e6 = Entry(t, width=50)
                    e6.place(x=350, y=180, height=35)
                
                    l9 = Label(t, text='Contact Number :', font=('Times New Roman', 20))
                    l9.place(x=120, y=250)
                    e7 = Entry(t, width=50)
                    e7.place(x=350, y=250, height=35)
                
                    l10 = Label(t, text='Select Gender :', font=('Times New Roman', 20))
                    l10.place(x=120, y=330)
                    r1 = Radiobutton(t, text='Male', variable=x, command=change, value=0)
                    r2 = Radiobutton(t, text='Female', variable=x, command=change, value=1)
                    r3 = Radiobutton(t, text='Others', variable=x, command=change, value=2)
                    r1.place(x=350, y=300)
                    r2.place(x=350, y=330)
                    r3.place(x=350, y=360)
                
                    l11 = Label(t, text='Select Country :', font=('Times New Roman', 20))
                    l11.place(x=120, y=400)
                    cb = ttk.Combobox(t)
                    c = ['India', 'Canada', 'Germany', 'Brazil', 'Bangladesh']
                    cb['values'] = c
                    cb.place(x=350, y=400, width=150, height=30)
                
                    l12 = Label(t, text='Enter Password :', font=('Times New Roman', 20))
                    l12.place(x=120, y=450)
                    e8 = Entry(t, width=50)
                    e8.place(x=350, y=450, height=35)
                
                    l13 = Label(t, text='Re-enter Password :', font=('Times New Roman', 20))
                    l13.place(x=120, y=500)
                    e9 = Entry(t, width=50)
                    e9.place(x=350, y=500, height=35)
                
                    bt6 = Button(t, text='REGISTER', font=('Lucida Handwritng', 20),command=RegInt)
                    bt6.place(x=500, y=550)
           
            def forg():
                        t = tkinter.Tk()
                        t.geometry('700x700')
                        t.config(bg='light blue')
                        t.title('Forgot Password Screen')
                
            l4 = Label(t, text='New Password :', font=('Lucida Handwriting', 20))
            l4.place(x=350, y=220)
            e3 = Entry(t, width=50)
            e3.place(x=760, y=220, height=35)
            
            l5 = Label(t, text='Confirm Password :', font=('Lucida Handwriting', 20))
            l5.place(x=350, y=330)
            e4 = Entry(t, width=50)
            e4.place(x=760, y=330, height=35)
                
            bt4 = Button(t, text='SAVE', font=('Lucida Handwriting', 20))
            bt4.place(x=580, y=440)
        '''        
                
    l1 = Label(t, text='ADMIN LOGIN PAGE', font=('Times new Roman', 20),
                               fg='grey', bg='light yellow', width=50, height=1)
    l1.place(x=350, y=50)
    l2 = Label(t, text='Admin Id :', font=('Times new roman', 20))
    l2.place(x=450, y=220)
    e1 = Entry(t, width=40, font=('Times new roman', 15))
    e1.place(x=650, y=220, height=35)
    l3 = Label(t, text='Password :', font=('Times New Roman', 20))
    l3.place(x=450, y=330)
    e2 = Entry(t, width=40, show='*', font=('Times new roman', 15))
    e2.place(x=650, y=330, height=35)
    bt1 = Button(t, text='LOGIN', font=('Times New Roman', 15),command=Ok)
    bt1.place(x=450, y=440)
    bt2 = Button(t, text='CANCEL', font=('Times New Roman', 15),command=t.destroy)
    bt2.place(x=670, y=440)
    '''
    bt3 = Button(t, text='FORGET PASSWORD', font=('Times New Roman', 15))
    bt3.place(x=670, y=440)
    bt5 = Button(t, text='REGISTER', font=('Times New Roman', 15))
    bt5.place(x=900, y=440)
    '''
    t.mainloop() 
frontone()