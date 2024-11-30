from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Initialize the main window
root = Tk()
root.title('Rock Paper Scissor')
root.configure(background="#A1662F")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_computer_img = ImageTk.PhotoImage(Image.open("rock_computer.png"))
paper_computer_img = ImageTk.PhotoImage(Image.open("paper_computer.png"))
scissor_computer_img = ImageTk.PhotoImage(Image.open("scissor_computer.png"))

# Labels for images
user_label = Label(root, image=scissor_img, bg="#A1662F")
computer_label = Label(root, image=scissor_computer_img, bg="#A1662F")
computer_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Score labels
player_score = Label(root, text=0, font=("Arial", 16), bg="#A1662F", fg="white")
computerScore = Label(root, text=0, font=("Arial", 16), bg="#A1662F", fg="white")
computerScore.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=("Arial", 14), text="USER", bg="#A1662F", fg="white")
user_indicator.grid(row=0, column=3)
computer_indicator = Label(root, font=("Arial", 14), text="COMPUTER", bg="#A1662F", fg="white")
computer_indicator.grid(row=0, column=1)

# Message label
msg = Label(root, text="Make a choice!", font=("Arial", 14), bg="#A1662F", fg="white")
msg.grid(row=3, column=2)

# Update message
def update_msg(x):
    msg['text'] = x

# Update user score
def updateuserscore():
    score = int(player_score['text'])
    score += 1
    player_score["text"] = str(score)

# Update computer score
def updatecomputerscore():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] = str(score)

# Check winner
def checkWinner(player, computer):
    if player == computer:
        update_msg("It's a Tie!🤝")
    elif player == "rock":
        if computer == "paper":
            update_msg("You Lose!😢")
            updatecomputerscore()
        else:
            update_msg("You Win!🎉")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            update_msg("You Lose!😢")
            updatecomputerscore()
        else:
            update_msg("You Win!🎉")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            update_msg("You Lose!😢")
            updatecomputerscore()
        else:
            update_msg("You Win!🎉")
            updateuserscore()

# Update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    # Computer choice
    computer_choice = choices[randint(0, 2)] 
    if computer_choice == "rock":
        computer_label.configure(image=rock_computer_img)
    elif computer_choice == "paper":
        computer_label.configure(image=paper_computer_img)
    else:
        computer_label.configure(image=scissor_computer_img)

    # User choice
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWinner(x, computer_choice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

# Run the main loop
root.mainloop()
