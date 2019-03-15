from tkinter import *
from tkinter import messagebox

import tkinter


def execute():
    import donottouch
    import finalfking
    import time
    progress['value']=20
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=50
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=80
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=100
    progress.pack()

def write():
    text=iptxt.get("1.0","end")
    file = open("user.txt",'w')
    file.write(text)
    file.close()

def example():
    messagebox.showinfo("Example", "EXAMPLE")

def readme():
    # create child window
    win = Toplevel()
    # display message
    message = "This is the child window"
    Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()

def displaynigga():
    disp=Toplevel()
    disp.geometry("800x900")
    heading = Label(disp, text="ASCG | Automatic Source Code Generator",font=("times new roman",20,"italic")).pack()
    textinfile=""
    file=open("finaloutput.txt","r")
    for i in file:
        textinfile=textinfile+i
    txt = Text(disp, height=40, width=90,wrap=WORD)
    txt.place(x=10,y=60)
    txt.delete('1.0', END)
    txt.insert(INSERT,textinfile)
    scrollb = tkinter.Scrollbar(disp, command=txt.yview)
    txt['yscrollcommand'] = scrollb.set


    
root = Tk()

root.title("ASCG")
root.geometry("600x680")

heading = Label(root, text="ASCG | Automatic Source Code Generator",font=("times new roman",20,"italic")).pack()

iphead = Label(root, text="Enter Input:",font=("arial",10,"bold")).place(x=5, y=40)
iptxt = Text(root, height=30, width=50, wrap = WORD)
iptxt.place(x=10,y=60)

cf = Button(root, text="Create File",command=write,height = 3, width = 15,font=('helvetica',10, 'bold'))
cf.place(x=423, y=60)

cp = Button(root, text="Compile",command=execute,height = 3, width = 15,font=('helvetica',10, 'bold'))
cp.place(x=423, y=120)

run = Button(root, text="Run",command=displaynigga,height = 3, width = 15,font=('helvetica',10, 'bold'))
run.place(x=423, y=180)

ex = Button(root, text="Example", command=example,height = 3, width = 15,font=('helvetica',10, 'bold'))
ex.place(x=423, y=240)

rm = Button(root, text="Read Me", command=readme,height = 3, width = 15,font=('helvetica',10, 'bold'))
rm.place(x=423, y=300)

exit = Button(root, text="Exit",fg="red", command=lambda:root.destroy(),height = 3, width = 15,font=('helvetica',10, 'bold'))
exit.place(x=423, y=360)

db = Label(root, text="Developed By: \n-1\n-2\n-3\n-4",font=("times new roman",15,"italic")).place(x=5, y=550)
    
root.mainloop()
