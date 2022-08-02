import tkinter
from tkinter import *
#from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from empinsert import *
from empinsert import *
from empUpdate import *
from empFind import *
from empDelete import *
from amsInsert import*
from amsUpdate import*
from amsFind import*
from amsDelete import*
from depInsert import *
from depUpdate import *
from depFind import *
from depDelete import *
from workInsert import *
from workUpdate import *
from workFind import *
from workDelete import *
from holidayInsert import *
from holidayUpdate import *
from holidayFind import *
from holidayDelete import *

'''
img=ImageTk.PhotoImage(Image.open("Admin1.jpg"))
lbl=Label(c,image=img)
lbl.place(x=0,y=0)
'''  
#pic1=PhotoImage(file="E:\Python projects\Employee attendance system\insert3.png")
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
b13=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=holione)
b13.place(x=30,y=530)
b14=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=holitwo)
b14.place(x=30,y=560)
b15=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=holithree)
b15.place(x=30,y=590)
b16=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=holifour)
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
