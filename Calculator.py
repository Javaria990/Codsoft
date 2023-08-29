from tkinter import *
def click(event):
    global values
    text=event.widget.cget('text')
    if text=="=":
        if values.get().isdigit():
            value=int(values.get())
        else:
            try:
                value = eval(values.get())
            except Exception as e:
                print(e)
                value = "Error"
            values.set(value)
            screen.update()
    elif text=="C":
        values.set("")
        screen.update()
    elif text=="OFF":
        root.quit()
    elif text == "x":
        values.set(str(values.get()) + "*")
        screen.update()
    elif text == "÷":
        values.set(str(values.get()) + "/")
        screen.update()
    else:
        values.set(str(values.get())+str(text))
        screen.update()
root = Tk()
root.geometry('320x480')
root.minsize(320,480)
root.maxsize(320,480)
root.title('Standard Calculator By Javaria')
Label(root,text="Standard Calculator!",font="TimesNewRoman 24 italic bold",bg="dark slate gray",fg="white").pack()
screen_frame = Frame(root,borderwidth=2,relief=RIDGE,bg="gray59")
values = StringVar()
values.set("")
screen=Entry(screen_frame,textvar=values,font="lucida 40 bold")
screen.pack(pady=2)
screen_frame.pack()
nu_but_fr = Frame(root)
b1=Button(nu_but_fr, text='OFF', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2,padx=41, relief=GROOVE,background='dark slate grey')
b1.pack(side=LEFT,anchor='s')
b1.bind("<Button-1>",click)
b3=Button(nu_but_fr, text='C', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='dark slate grey')
b3.pack(side=LEFT,anchor='s')
b3.bind("<Button-1>",click)
b3=Button(nu_but_fr, text='÷', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='dark slate grey')
b3.pack(side=LEFT,anchor='s')
b3.bind("<Button-1>",click)
nu_but_fr.pack(anchor='w')
nuo_but_fr = Frame(root)
b1 = Button(nuo_but_fr, text='x', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='dark slate grey')
b1.pack(side=TOP, anchor='s')
b1.bind("<Button-1>",click)
b2 = Button(nuo_but_fr, text='-', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='dark slate grey')
b2.pack(side=TOP, anchor='s')
b2.bind("<Button-1>",click)
b3 = Button(nuo_but_fr, text='+', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2,pady=39,relief=GROOVE,background='dark slate grey')
b3.pack(side=TOP, anchor='s')
b3.bind("<Button-1>",click)
nuo_but_fr.pack(side=RIGHT, fill=Y, padx=0)
num3_but_fr = Frame(root)
for button in range(7, 10):
    btn = Button(num3_but_fr, text=button, font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief="ridge")
    btn.grid(row=1, column=button-3)
    btn.bind("<Button-1>", click)
num3_but_fr.pack(anchor='w')
num2_but_fr = Frame(root)
for button in range(4, 7):
    btn = Button(num2_but_fr, text=button, font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief="ridge")
    btn.grid(row=1, column=button - 3)
    btn.bind("<Button-1>",click)
num2_but_fr.pack(anchor='w')
num_but_frame = Frame(root)
for button in range(1, 4):
    btn = Button(num_but_frame, text=button, font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief="ridge")
    btn.grid(row=1, column=button)
    btn.bind("<Button-1>", click)
num_but_frame.pack(anchor='w')
nu_but_fr = Frame(root)
b1=Button(nu_but_fr, text='.', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='gray23')
b1.pack(side=LEFT,anchor='s')
b1.bind("<Button-1>",click)
b2=Button(nu_but_fr, text='0', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief="ridge")
b2.pack(side=LEFT,anchor='s')
b2.bind("<Button-1>",click)
b3=Button(nu_but_fr, text='=', font=("Helvetica", 17, "bold"), fg='white', bg='black', width=5, height=2, relief=GROOVE,background='gray23')
b3.pack(side=LEFT,anchor='s')
b3.bind("<Button-1>",click)
nu_but_fr.pack(anchor='w')
root.mainloop()
