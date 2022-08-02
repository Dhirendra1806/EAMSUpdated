import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import datetime


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
                
            s = "Select ename from employee where empid=%s",(password,uname)
            cur.execute(s)
            messagebox.showinfo("", "Your Attendance has been marked")
            data=cur.fetchone()
            if data:
                messagebox.showinfo("Info","Login Succssfull")
            else:
                messagebox.showerror("Info","Login failed")
            db.commit()
            db.close()
        
'''
            def amsmark():
            
                    db = pymysql.connect(host='localhost', user='root',
                                             password='root', database='company')
                    cur = db.cursor()
                    a=e1.get()
                    b=e2.get()
                    c=e3.get()
                    
                    s = "insert into ams values('%s','%s','%s')" % (
                        a, b, c)
                    cur.execute(s)
                        
                    messagebox.showinfo("", "Your Attendance has been marked")
                    db.close()
                    
                    '''  
               
                
              
                              
        
        
def clear():
        t.destroy()
    
    
         
        
    
    

    
    
l1 = Label(t, text='USER LOGIN PAGE', font=('Times new Roman', 20),
               fg='grey', bg='light yellow', width=50, height=1)
l1.place(x=350, y=50)
l2 = Label(t, text='Employee ID :', font=('Times new roman', 20))
l2.place(x=450, y=220)
e1 = Entry(t, width=50)
e1.place(x=650, y=220, height=35)
l3 = Label(t, text='Password :', font=('Times New Roman', 20))
l3.place(x=450, y=330)
e2 = Entry(t, width=50, show='*')
e2.place(x=650, y=330, height=35)
    
d = datetime.datetime.now()

    
e3 = Entry(t, width=50,font=('Times new roman',20))
e3.place(x=1, y=1, height=35)
e3.insert(END, d.strftime('%Y-%m-%d  %A %H:%M:%S'))


    
bt1 = Button(t, text='OK', font=('Times New Roman', 15),command=Ok)
bt1.place(x=580, y=440)
bt2 = Button(t, text='CANCEL', font=('Times New Roman', 15),command=clear) 
bt2.place(x=690, y=440) 
'''bt4 = Button(t, text='FORGOT PASSWORD', font=('Times New Roman', 15),command=forg) 
    bt4.place(x=750, y=540) '''
t.mainloop()
