from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title('Rock Paper Scissor')
root.configure(background="#A1662F")



rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_computer_img = ImageTk.PhotoImage(Image.open("rock_computer.png"))
paper_computer_img = ImageTk.PhotoImage(Image.open("paper_computer.png"))
scissor_computer_img = ImageTk.PhotoImage(Image.open("scissor_computer.png"))






root.mainloop()