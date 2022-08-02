import tkinter
from tkinter import *
#from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
import datetime

def attend():
    db = pymysql.connect(host='localhost', user='root',
                         password='root', database='company')
    cur = db.cursor()
    a = e2.get()
    c = e3.get()
    d = x1.get()
    e = e5.get()
    
    
    s = "insert into amsone values('%s','%s','%s','%s')" % (
        a, c, d, e)
    
    cur.execute(s)
    d = datetime.datetime.now()

    
    e6.insert(0, d.strftime('%Y-%m-%d  %A %H:%M:%S'))
    print(d)
    db.commit()
    
    
    messagebox.showinfo("Data saved", "Saved")
    
    e2.delete(0, 100)
    e3.delete(0, 100)
    x1.delete(0, 100)
    e5.delete(0, 100)
    e6.delete(0, 100)
    e7.delete(0,100)
    db.close()
    
def OK():
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        
        s="select * from amsone" 
        cur.execute(s)
        
        data=cur.fetchall()
        
        for row in data:
            
            
    
            tree.insert("", tk.END, values=row)        
    
        db.close()

c=Canvas(width=1550,height=800,bg='lightblue')
c.place(x=0,y=0)
        
l0 = Label(c, text='Welcome to Attendance pannel', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
l0.place(x=50, y=0)
        
l1=Label(c,text='Employee Details',font=('Times new roman',15))
l1.place(x=50,y=70)
        
l2=Label(c,text='Employee ID:',font=('Times new roman',15))
l2.place(x=50,y=130)
e2 = Entry(c, width=20)
e2.place(x=200, y=130, height=30)
    
    
    
l3=Label(c,text='Employee Name',font=('Times new roman',15))
l3.place(x=50,y=190)
e3 = Entry(c, width=40)
e3.place(x=200, y=190, height=30)
    
    
    
l5=Label(c,text='Dept ID:',font=('Times new roman',15))
l5.place(x=480,y=190)
e5 = Entry(c, width=20)
e5.place(x=620, y=190, height=30)
    
    
l6=Label(c,text='Time/date :',font=('Times new roman',15))
l6.place(x=50,y=250)
e6 = Entry(c, width=40)
e6.place(x=200, y=250, height=30)
    
    
l7=Label(c,text='Day : ',font=('Times new roman',15))
l7.place(x=480,y=250)
e7 = Entry(c, width=30)
e7.place(x=600, y=250, height=30)

    
l8=Label(c,text='Attend status : ',font=('Times new roman',15))
l8.place(x=150,y=350)

x1=IntVar()
a=ttk.Combobox(c, width=30,textvariable=x1)
a.place(x=300,y=350, height=30)
a['values']=('Present')

    
    
tree = ttk.Treeview(c, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
    
tree.column("#1")
tree.heading("#1", text="Employee ID")
    
tree.column("#2")
tree.heading("#2", text="Employee name")
    
tree.column("#3")
tree.heading("#3", text="Dept ID:")
    
tree.column("#4")
tree.heading("#4", text="Time/Date")
    
tree.column("#5")
tree.heading("#5", text="Day")
    
tree.column("#6")
tree.heading("#6", text="Attend Status")
    
button1 = Button(c,text="Display data", command=OK)

button1.place(x=100,y=400)

button2 = Button(c,text="Attend", command=attend)

button2.place(x=200,y=400)

    
tree.pack(pady=500)
    
c.mainloop()
    
    
