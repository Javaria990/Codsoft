from tkinter import *
import random
def copy_to_clipboard():
    value = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(value)
    root.update()
def yes(string, value):
    c = ""
    value = int(value)
    for i in range(value):
        c += random.choice(string)
    print(c)
    return c
def click(event):
    global password
    s = ""
    abab = a_var.get()
    cdcd = b_var.get()
    efef = c_var.get()
    ghgh = d_var.get()
    ijij = my.get()
    if abab == 1:
        s += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if cdcd == 1:
        s += "abcdefghijklmnopqrstuvwxyz"
    if efef == 1:
        s += "123456789"
    if ghgh == 1:
        s += "!@#$%^&*()_+=-|\|/.,?><"
    print(password)
    length = my.get()
    password = yes(s, length)
    password_entry.config(state=NORMAL)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password_entry.config(state=DISABLED)
root = Tk()
root.configure(bg='white')
root.geometry("750x550")
root.title("Password Generator By Javaria!")
password=""
Label(root, text="Password Generator", font="Forte 23 bold underline", fg="DodgerBlue4",bg="white").pack(pady=4)
Label(root, text="Instantly generate a secure, random password with this Python tool", font="TimesNewRoman 15 bold",
      fg="DeepSkyBlue4",bg="white").pack()
Label(root, text="Empower your security with our sleek password generator app, crafting robust passwords effortlessly."
                , font="TimesNewRoman 11 bold", fg="DeepSkyBlue4",bg="white").pack()
Label(root, text="Shield your digital world with passwords as strong as they are unique."
                , font="TimesNewRoman 11 bold", fg="DeepSkyBlue4",bg="white").pack()
label_frame = Frame(root,bg="white")
label_frame.pack()
nam_la = Label(label_frame, text='Length of Characters', font="TimesNewRoman 11 bold underline",
               fg='DeepSkyBlue4',bg="white")
nam_la.grid(row=0, column=0)
my= Scale(label_frame, from_=0, to=50, orient=HORIZONTAL,width=17,bg="white",foreground="DeepSkyBlue4",relief=SUNKEN)
my.grid(row=0, column=1, padx=12)
sele_frame=Frame(root,bg="white")
a_var= IntVar()
a = Checkbutton(sele_frame, text="ABC - Capital Letters", variable=a_var,padx=1000, font="TimesNewRoman 11 bold",fg="DeepSkyBlue4",bg="white")
a.pack(padx=0)
b_var = IntVar()
b = Checkbutton(sele_frame, text="abc - Small Letters", variable=b_var, padx=1000, font="TimesNewRoman 11 bold",fg="DeepSkyBlue4",bg="white")
b.pack(padx=10)
c_var = IntVar()
c = Checkbutton(sele_frame, text="123 - Numbers", variable=c_var,padx=1000, font="TimesNewRoman 11 bold",fg="DeepSkyBlue4",bg="white")
c.pack(padx=10)
d_var = IntVar()
d = Checkbutton(sele_frame, text="@$/ - Special Characters", variable=d_var,padx=840,font="TimesNewRoman 11 bold", fg="DeepSkyBlue4",bg="white")
d.pack(padx=10)
sele_frame.pack()
b3=Button(root, text='Submit', font=("Helvetica", 11, "bold"), fg='white', bg='white',foreground="DeepSkyBlue4",width=12)
b3.pack(anchor='s')
b3.bind("<Button-1>",click)
Label(root, text="____________________________________________________________________________",font="TimesNewRoman 11 bold",fg="DeepSkyBlue4",bg="white").pack()
Label(root, text="\n Generated Password",font="TimesNewRoman 14 bold underline",fg="DeepSkyBlue4",bg="white").pack()
# Create the Treeview with an initial item
password_entry =Entry(root, state="readonly", disabledforeground="dark slate gray", disabledbackground="white",width=30)
password_entry.pack()
copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard,font="TimesNewRoman 11 bold",fg="DeepSkyBlue4",bg="white")
copy_button.pack(pady=5)
root.mainloop()
