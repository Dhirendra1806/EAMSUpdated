import tkinter
from tkinter import *

def userlogin():
t=tkinter.Tk()
t.geometry('600x600')


        t.title("User Login")
        l1=Label(t,text="User Login",fg='Red',font=('Times new roman',25))
        l1.place(x=200,y=50)
        
        l2=Label(t,text="Username:",fg='Red',font=('Times new roman',17))
        l2.place(x=100,y=170)
        
        e1=Entry(t,width=20,font=('Times new roman',17))
        e1.place(x=250,y=170)
        
        l3=Label(t,text="Password:",fg='Red',font=('Times new roman',17))
        l3.place(x=100,y=250)
        
        e2=Entry(t,width=20,font=('Times new roman',17))
        e2.place(x=250,y=250)
        
        bt1=Button(t,text='Login',width=8,font=('Times new roman',15))
        bt1.place(x=100,y=350)
        
        bt2=Button(t,text='Reset',width=8,font=('Times new roman',15))
        bt2.place(x=250,y=350)
        
        bt3=Button(t,text='Cancel',width=8,font=('Times new roman',15),command=t.destroy)
        bt3.place(x=400,y=350)
        
        
        
        t.config(bg='grey')
        t.mainloop()    
        
userlogin()