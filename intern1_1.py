#The game starts when u press the start button 
from tkinter import *
import random
#create the window
root=Tk()
root.title("Number Guessing Game")
root.geometry("650x450")
root.configure(bg='green')
chance_var=IntVar()
def new_game():
    global num,chance
    chance=0
    guessInput.delete(0,"end")
    comment.delete(0,"end")
    chanceentry.delete(0,"end")
    guessButton.config(state='normal')
    num=random.randint(1,100)
def play_game():
    global chance
    #takes input from user
    numguess=int(guessInput.get())
    chance+=1
    #if user number lessthan system generated number then
    if numguess<num:
        comment.delete(0,"end")
        comment.insert(0,"Hist:Try a higher number!")
    #if user number greaterthan system generated number then
    elif numguess>num:
        comment.delete(0,"end")
        comment.insert(0,"Hist:Try a lower number!")
        #if user and system generated number is equal then
    else:
        comment.delete(0,"end")
        comment.insert(0,"congratulations!you won")
        guessButton.configure(state='disabled')
    chance_var.set(chance)
#labels for headings and styling
textLabel=Label(text="Guess a number between 1 to 100",font=("Arial",20,"bold"),bg='PaleTurquoise2')
textLabel.grid(row=0,column=0)
guessInput=Entry(font=("bold",14),width=8)
guessInput.grid(row=2,column=0,padx=10,pady=10)
comment=Entry(font=("bold",14),bg='PaleTurquoise2',fg='navy',bd=0)
comment.grid(row=4,column=0,padx=20,pady=20)
chancelabel=Label(text="Number of Guesses you have made is:",font=("bold",14),bg='PaleTurquoise2')
chancelabel.grid(row=5,column=0)
chanceentry=Entry(font=("bold",14),width=4,textvariable=chance_var,bd=0,bg='PaleTurquoise2')
chanceentry.grid(row=5,column=0,sticky='e')
chanceentry.delete(0,"end")
startButton=Button(text="start/Restart Game",bg="blue",fg="white",font=("bold",14),command=new_game)
startButton.grid(row=1,column=0,padx=10,pady=20)
guessButton=Button(text="Guess",bg="magenta",fg="white",font=("bold",14),state='disabled',command=play_game)
guessButton.grid(row=3,column=0,padx=10,pady=10)
exitButton=Button(text="EXIT",bg="red",fg="white",font=("bold",14),command=root.destroy)
exitButton.grid(row=6,column=0,pady=20)
root.mainloop()
if True:
    print("succesfully Ran")
    
