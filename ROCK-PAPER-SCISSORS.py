from tkinter import *
import random
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
def getvals():
    admin()
def choice():
    s = ("Rock", "Paper", "Scissors")
    return random.choice(s)
def get_score():
    with open('marks.txt', 'r') as f:
        return int(f.read())
def update_score(score):
    with open('marks.txt', 'w') as f:
        f.write(str(score))
def admin():
    global result_var
    user_choice = ""
    if a_var.get():
        user_choice = "Rock"
    elif b_var.get():
        user_choice = "Paper"
    elif c_var.get():
        user_choice = "Scissors"
    comp_choice = choice()
    comp_choice_var.set(comp_choice)
    if user_choice == comp_choice:
        result="It's a tie"
    elif (user_choice == "Rock" and comp_choice=="Scissors") or \
            (user_choice=="Paper" and comp_choice=="Rock") or \
            (user_choice=="Scissors" and comp_choice=="Paper"):
        result="You Won"
        score = get_score()
        newscore =score + 1
        update_score(newscore)
    else:
        result="You Lose"
    result_var.set(result)
    score_label.config(text="Your Score is ... " + str(get_score())+"\n")

def open_feedback_window():
    def submit_feedback():
        user_feedback = feedback_entry.get()
        num=var.get()
        tmsg.showinfo("Feedback","Thanks for your Feedback")
        po=feed_entry.get()
        with open("feedback.txt","a") as f:
            f.write(f"{po}: {num} , {user_feedback}\n")

        feedback_window.destroy()

    feedback_window = Toplevel(root)
    feedback_window.geometry("300x190")
    feedback_window.title("Feedback")
    feed=Frame(feedback_window)
    feed.pack()
    feed_label = Label(feed, text="Name:",font="Forte 12", fg="dark slate gray")
    feed_label.grid(row=0,column=0,pady=10)
    feed_entry = Entry(feed)
    feed_entry.grid(row=0,column=1,pady=10)
    Label(feedback_window, text="Rate Us (among 5)!",font="Forte 13 underline", fg="dark slate gray").pack()
    okay=Frame(feedback_window)
    okay.pack()
    var = IntVar()
    Radiobutton(okay,text="1",variable=var, value=1).grid(row=1,column=0)
    Radiobutton(okay,text="2",variable=var, value=2).grid(row=1,column=1)
    Radiobutton(okay,text="3",variable=var, value=3).grid(row=1,column=2)
    Radiobutton(okay,text="4",variable=var, value=4).grid(row=1,column=3)
    Radiobutton(okay,text="5",variable=var, value=5).grid(row=1,column=4)
    feedback_label = Label(feedback_window, text="Please provide your feedback:",font="Forte 13 underline", fg="dark slate gray")
    feedback_label.pack()
    feedback_entry = Entry(feedback_window)
    feedback_entry.pack()
    submit_button = Button(feedback_window, text="Submit Feedback", command=submit_feedback,font="Forte 13 underline", fg="dark slate gray")
    submit_button.pack(pady=13)
root=Tk()
root.configure(bg="dark slate gray")
root.title("Rock Paper Scissors")
Label(root, text="Rock Paper Scissors", pady=50, bg="dark slate gray",
      font="TimesNewRoman 27 bold underline italic", fg="white").grid(row=0, column=1, padx=20)
mele_frame = Frame(root,background="dark slate gray")
mele_frame.grid(row=1, column=0, padx=0)
sele_frame = Frame(root)
sele_frame.grid(row=1, column=1, padx=20)
lele_frame = Frame(root, background="dark slate gray")
lele_frame.grid(row=1, column=2, padx=40)
Label(mele_frame,text="Instructions",font="TimesNewRoman 12 bold italic",foreground="white",background="dark slate gray").pack()
Label(mele_frame, text="⁎⁎⁎Welcome to Rock Paper Scissors Game!⁎⁎⁎ \n Are you ready to test your luck and strategicthinking"
                       "\n This age-old challenge pits you against the \ncomputer in a battle of wits. \n Choose your move wisely, and see if you can outsmart \n your digital opponent. Are you up for the challenge? Let's dive in! \n1.Objective: The goal of the game is to predict and \n choose a move that will beat the computer's choice.\n 2.Moves:\n ‣Rock: Beats scissors, loses to paper.\n ‣Paper: Beats rock, loses to scissors.\n ‣Scissors: Beats paper, loses to rock. 3.Gameplay:\n •You can select your move by clicking the \n checkboxes labeled 'Rock', 'Paper,' or 'Scissors' \n under  the 'Your Choice' section.\n•After making your choice, click the 'Submit' button.\n•The computer will then randomly choose its move.\n•The computer's \n choice will be displayed in the 'Computer's Choice' section\n.•The final result of the round will be shown \n in the 'Final Results section. You'll find\n out whether you won, lost, or tied against the computer.\n Outcome:\n If your choice defeats the computer's choice, you win!\n If the computer's choice defeats your choice, you lose.\n If both you and the computer make the same choice, it's a tie.\n Remember, Rock Paper Scissors is a game of chance and \n strategy.\nLet the games begin!",bg="dark slate gray",fg="white",font="TimesNewRoman 10 ").pack(anchor="w")
pil_image=Image.open("png-transparent-rock-paper-scissors-scissors-stone-cloth-thumbnail-removebg-preview.png")
image=ImageTk.PhotoImage(pil_image)
image_label=Label(sele_frame, image=image, bg="dark slate gray")
image_label.pack()
score_label=Label(lele_frame, text="Your Score is ... " + str(get_score())+"\n",
                    fg="white", background="dark slate gray", font="TimesNewRoman 16 bold ")
score_label.pack()
Label(lele_frame, text="Choose only one option at a Time", background="dark slate gray", fg="white", font="TimesNewRoman 12 italic underline").pack(pady=10)
Label(lele_frame, text="Your Choice", background="dark slate gray", fg="white", font="TimesNewRoman 16 bold ").pack()
h = Frame(lele_frame, background="dark slate gray")
h.pack()
a_var=IntVar()
a=Checkbutton(h, text="Rock  ", variable=a_var, background="dark slate gray",font="TimesNewRoman 11 bold italic",fg="black")
a.grid(row=2, column=1)
b_var=IntVar()
b=Checkbutton(h, text="Paper  ", variable=b_var, background="dark slate gray",font="TimesNewRoman 11 bold italic",fg="black")
b.grid(row=2, column=2)
c_var=IntVar()
c = Checkbutton(h, text="Scissors", variable=c_var, background="dark slate gray",font="TimesNewRoman 11 bold italic",fg="black")
c.grid(row=2, column=3)
Button(lele_frame, text="Submit", command=getvals,foreground="black").pack(pady=10)
Label(lele_frame, text="Computer's Choice",font="TimesNewRoman 16 bold",bg="dark slate gray",fg="white").pack(pady=10)
comp_choice_var=StringVar(value="")
comp_choice_entry=Entry(lele_frame, textvariable=comp_choice_var, state="disabled",
                          disabledforeground="dark slate gray", disabledbackground="white")
comp_choice_entry.pack()
Label(lele_frame, text="Final Results",font="TimesNewRoman 17 bold underline",bg="dark slate gray",fg="white").pack(pady=10)
result_var=StringVar(value="")
result_label=Label(lele_frame, textvariable=result_var,bg="dark slate gray",font="TimesNewRoman 25 bold",fg="white")
result_label.pack()
Button(lele_frame,text="Your Feedback",command=open_feedback_window).pack(pady=10)
root.mainloop()
