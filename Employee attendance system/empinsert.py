import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql

def Empone():
    

    def empInsert():
        
            
        
        if len(e1.get())==0:
            
            e1.config(bg='Red')
            e2.config(bg='Red')
            e3.config(bg='Red')
            e4.config(bg='Red')
            e5.config(bg='Red')
            e6.config(bg='Red')
            messagebox.showwarning("Warning","please fill it all")

        name = e2.get()
        msg = ''

        if len(name) == 0:
            msg = 'name can\'t be empty'
        else:
            try:
                if any(ch.isdigit() for ch in name):
                    msg = 'Name can\'t have numbers'
                elif len(name) <= 2:
                    msg = 'name is too short.'
                elif len(name) > 100:
                    msg = 'name is too long.'
                else:
                    msg = 'Success!'
            except Exception as ep:
                messagebox.showerror('error', ep)
        
        messagebox.showinfo('message', msg)
        
        
        
        me = e4.get()
        if me == '':
            msg = 'provide Mobile num '
        else:
            try:
                if any(ch.isdigit() for ch in me):
                    if len(me) == 10:
                        int(me)
                        msg = 'success'
                    else:
                        msg = 'incorrect mobile number!'
                else:
                        msg = 'success!'
            except Exception as ep:
                msg = ep
                messagebox.showinfo('message', msg)    
              
        special_ch = ['@', '.']
        msg = ''
        phone = e5.get()
        if phone == '':
            msg = 'provide Mobile num or Email'
        else:
            try:
                if not any(ch in special_ch for ch in me):
                    msg = 'incorrect email!'
                else:
                    db = pymysql.connect(host='localhost', user='root',
                                         password='root', database='company')
                    cur = db.cursor()
                    a = e1.get()
                    b = e2.get()
                    c = e3.get()
                    d = e4.get()
                    e = e5.get()
                    f = e6.get()
                    
                    s = "insert into employee values('%s','%s','%s','%s','%s','%s')" % (
                        a, b, c, d, e, f)
                    cur.execute(s)
                    db.commit()
                    messagebox.showinfo("Data saved", "Saved")
                    e1.delete(0, 100)
                    e2.delete(0, 100)
                    e3.delete(0, 100)
                    e4.delete(0, 100)
                    e5.delete(0, 100)
                    e6.delete(0, 100)
                    
                    db.close()
            except Exception as ep:
                msg = ep
                messagebox.showinfo('message', msg)    
        
                
    def correct(inp):
          if inp.isdigit():
              return True
             
          elif inp == "":
              return True
          else:
              return False  
              
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select Deptid from department" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    
    def filldataP():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select planid from wplan" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
   
            
    
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
    
    l1 = Label(c,text='EMPLOYEE DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Employee Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    e1 = Entry(c, width=50)
    e1.place(x=350, y=120, height=30)
    
    l3 = Label(c, text='Employee Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=350, y=180, height=30)
    
    l4 = Label(c, text='Address :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=350, y=240, height=30)
    
    l4 = Label(c, text='Phone No. :', font=('Times new roman', 20))
    l4.place(x=120, y=300)
    e4 = Entry(c, width=50)
    e4.place(x=350, y=300, height=30)
    reg = c.register(correct)
    e4.config(validate="key",validatecommand=(reg,'%P'))
    
    
    l5 = Label(c, text='Email :', font=('Times new roman', 20))
    l5.place(x=120, y=360)
    e5 = Entry(c, width=50)
    e5.place(x=350, y=360, height=30)
    
    l6 = Label(c, text='Department Id :', font=('Times new roman', 20))
    l6.place(x=120, y=420)
    e6=ttk.Combobox(c, width=50)
    e6.place(x=350,y=420, height=30)
    data=filldata()
    e6['values']=data
    
    def on_click_e1(event):
        e1.configure(state=NORMAL)
        e1.delete(0, END)
        e1.unbind('<Button-1>', on_click_id1)

    def on_click_e2(event):
        e2.configure(state=NORMAL)
        e2.delete(0, END)
        e2.unbind('<Button-1>', on_click_id2)

    def on_click_e3(event):
        e3.configure(state=NORMAL)
        e3.delete(0, END)
        e3.unbind('<Button-1>', on_click_id3)
    def on_click_e4(event):
        e4.configure(state=NORMAL)
        e4.delete(0, END)
        e4.unbind('<Button-1>', on_click_id4)

    def on_click_e5(event):
        e5.configure(state=NORMAL)
        e5.delete(0, END)
        e5.unbind('<Button-1>', on_click_id5)

    def on_click_e6(event):
        e6.configure(state=NORMAL)
        e6.delete(0, END)
        e6.unbind('<Button-1>', on_click_id6)
    
    
    
    
    
    # adding placeholders
    e1.insert(0, 'Employee ID:')
    e1.configure(state=DISABLED)
    e2.insert(0, 'Employee name')
    e2.configure(state=DISABLED)
    e3.insert(0, 'Address')
    e3.configure(state=DISABLED)
    e4.insert(0, '1234567890')
    e4.configure(state=DISABLED)
    e5.insert(0, 'Example@gmail.com')
    e5.configure(state=DISABLED)
    e6.insert(0, 'Department ID:')
    e6.configure(state=DISABLED)
    
    #binding placeholders
    e1.bind('<Button-1>', on_click_e1)
    e2.bind('<Button-1>', on_click_e2)
    e3.bind('<Button-1>', on_click_e3)
    e4.bind('<Button-1>', on_click_e4)
    e5.bind('<Button-1>', on_click_e5)
    e6.bind('<Button-1>', on_click_e6)



    on_click_id1 = e1.bind('<Button-1>', on_click_e1)
    on_click_id2 = e2.bind('<Button-1>', on_click_e2)
    on_click_id3 = e3.bind('<Button-1>', on_click_e3)
    on_click_id4 = e4.bind('<Button-1>', on_click_e4)
    on_click_id5 = e5.bind('<Button-1>', on_click_e5)
    on_click_id6 = e6.bind('<Button-1>', on_click_e6)

    
    
   
   
    
    
    bt = Button(c, text='SAVE', width=40, height=1,font=('Times new roman',15),command=empInsert)
    bt.place(x=500, y=550)
    
