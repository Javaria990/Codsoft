from tkinter import *
import datetime
def add_text():
    namef = namevalue.get()
    with open('todo-list.txt', 'a') as f:
        f.write(namef + '\n')
    namevalue.set('')
    update_text()
def update_text():
    with open('todo-list.txt', 'r') as f:
        tasks = f.readlines()
        text_area.config(state=NORMAL)
        text_area.delete('1.0', END)
        for task in tasks:
            text_area.insert(END, task)
        text_area.config(state=DISABLED)
def clear_text():
    with open('todo-list.txt', 'w') as f:
        f.write("")
    update_text()
def show_text():
    update_text()
root = Tk()
root.title("To-Do-List By Javaria!")
root.geometry('350x500')
root.minsize(350, 500)
Label(root, text="TO-DO-LIST", font="TimesNewRoman 20 italic bold underline", fg="dark slate gray", pady=10).pack()
text_frame = Frame(root, background='dark slate gray', borderwidth=6, relief=FLAT)
text_frame.pack(side=TOP, fill=BOTH, expand=False, padx=20, pady=10)
text_area = Text(text_frame, wrap=WORD, state=DISABLED, height=15)
text_area.pack(fill=BOTH, expand=False)
label_frame = Frame(root)
label_frame.pack()
nam_la = Label(label_frame, text='Name',font="TimesNewRoman 10 bold underline",fg='dark slate gray')
nam_la.grid(row=0, column=0,pady=15)
namevalue = StringVar()
nameentry = Entry(label_frame, textvariable=namevalue, width=30)
nameentry.grid(row=0, column=1, padx=0, pady=0)
button_frame = Frame(root)
button_frame.pack()
add_button = Button(button_frame, text="Add Task",font="TimesNewRoman 10 bold",fg='dark slate gray', command=add_text, width=10)
add_button.pack(side=LEFT, padx=0, pady=10)
show_button = Button(button_frame, text="Show Tasks",font="TimesNewRoman 10 bold",fg='dark slate gray', command=show_text, width=10)
show_button.pack(side=LEFT, padx=0, pady=10)
clear_button = Button(button_frame, text="Clear Tasks",font="TimesNewRoman 10 bold",fg='dark slate gray', command=clear_text, width=10)
clear_button.pack(side=LEFT, padx=0, pady=10)
exit_button = Button(button_frame, text="Exit",fg='dark slate gray',font="TimesNewRoman 10 bold", command=root.quit, width=10)
exit_button.pack(side=LEFT, padx=0, pady=10)
root.mainloop()
