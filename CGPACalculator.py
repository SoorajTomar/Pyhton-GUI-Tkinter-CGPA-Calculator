from tkinter import *
from tkinter import messagebox
from functools import *
root=Tk()
root.title('CGPA Calculator')
root.geometry('300x300')
def f1(l1,l2):
    c=0.0
    j=0
    for i in l1:
        if i=='O':
            c+=10*l2[j]
        elif i=='A+':
            c+=9*l2[j]
        elif i=='A':
            c+=8*l2[j]
        elif i=='B':
            c+=7*l2[j]
        elif i=='C':
            i+=6*l2[j]
        elif i=='D':
            i+=5*l2[j]
        elif i=='P':
            c+=4.5*l2[j]
        else:
            c+=0
        j+=1
    x1=reduce(lambda x,y:x+y,l2)
    res="{:.2f}".format(c/x1)
    return str(res)
def f():
    list1=[v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get()]
    list2=[int(c1.get()),int(c2.get()),int(c3.get()),int(c4.get()),int(c5.get()),int(c6.get()),int(c7.get())]
    s='Your CGPA is '+f1(list1,list2)
    msg=messagebox.showinfo('CGPA',s)
l1=Label(root,text='Subject 1: SEPM')
l2=Label(root,text='Subject 2: PQT')
l3=Label(root,text='Subject 3: OS')
l4=Label(root,text='Subject 4: SE')
l5=Label(root,text='Subject 5: CC')
l6=Label(root,text='Subject 6: DAA')
l7=Label(root,text='Subject 7: APP')
l8=Label(root,text='Subject 8: CCTS')
l9=Label(root,text='Subject 9: ES')
v1=StringVar(root)
v2=StringVar(root)
v3=StringVar(root)
v4=StringVar(root)
v5=StringVar(root)
v6=StringVar(root)
v7=StringVar(root)
v8=StringVar(root)
v9=StringVar(root)
e1=OptionMenu(root,v1,"O","A+","A","B","C","D","P","F")
e2=OptionMenu(root,v2,"O","A+","A","B","C","D","P","F")
e3=OptionMenu(root,v3,"O","A+","A","B","C","D","P","F")
e4=OptionMenu(root,v4,"O","A+","A","B","C","D","P","F")
e5=OptionMenu(root,v5,"O","A+","A","B","C","D","P","F")
e6=OptionMenu(root,v6,"O","A+","A","B","C","D","P","F")
e7=OptionMenu(root,v7,"O","A+","A","B","C","D","P","F")
e8=OptionMenu(root,v8,"O","A+","A","B","C","D","P","F")
e9=OptionMenu(root,v9,"O","A+","A","B","C","D","P","F")
s1=StringVar(root,value='Credits')
s2=StringVar(root,value='0')
s3=StringVar(root,value='0')
s4=StringVar(root,value='0')
s5=StringVar(root,value='0')
s6=StringVar(root,value='0')
s7=StringVar(root,value='0')
s8=StringVar(root,value='0')
s9=StringVar(root,value='0')
c1=Entry(root,textvariable=s1)
c2=Entry(root,textvariable=s2)
c3=Entry(root,textvariable=s3)
c4=Entry(root,textvariable=s4)
c5=Entry(root,textvariable=s5)
c6=Entry(root,textvariable=s6)
c7=Entry(root,textvariable=s7)
c8=Entry(root,textvariable=s8)
c9=Entry(root,textvariable=s9)
l1.grid(sticky='w',row=0,column=0)
l2.grid(sticky='w',row=1,column=0)
l3.grid(sticky='w',row=2,column=0)
l4.grid(sticky='w',row=3,column=0)
l5.grid(sticky='w',row=4,column=0)
l6.grid(sticky='w',row=5,column=0)
l7.grid(sticky='w',row=6,column=0)
l8.grid(sticky='w',row=7,column=0)
l9.grid(sticky='w',row=8,column=0)
e1.grid(sticky='w',row=0,column=1)
e2.grid(sticky='w',row=1,column=1)
e3.grid(sticky='w',row=2,column=1)
e4.grid(sticky='w',row=3,column=1)
e5.grid(sticky='w',row=4,column=1)
e6.grid(sticky='w',row=5,column=1)
e7.grid(sticky='w',row=6,column=1)
e8.grid(sticky='w',row=7,column=1)
e9.grid(sticky='w',row=8,column=1)
c1.grid(sticky='w',row=0,column=2)
c2.grid(sticky='w',row=1,column=2)
c3.grid(sticky='w',row=2,column=2)
c4.grid(sticky='w',row=3,column=2)
c5.grid(sticky='w',row=4,column=2)
c6.grid(sticky='w',row=5,column=2)
c7.grid(sticky='w',row=6,column=2)
c8.grid(sticky='w',row=7,column=2)
c9.grid(sticky='w',row=8,column=2)
b1=Button(root,text='Calculate',command=f)
b1.grid(sticky='w',row=9,column=1)
root.mainloop()