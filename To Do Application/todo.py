from tkinter import *
from tkinter import ttk
import os 

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x500+300+150')

        self.label = Label(
            self.root,
            text='To-Do-List-App',
            font=('Helvetica', 40, 'bold'),
            bg='black',
            fg='white'
        )
        self.label.pack(side='top', fill=BOTH)
        self.label2 = Label(
            self.root,
            text='Add Task',
            font=('Helvetica', 30, 'bold'),
            bg='black',
            fg='white'
        )
        self.label2.place(x=40, y=80)
        self.label3 = Label(
            self.root,
            text='Tasks',
            font=('Helvetica', 30, 'bold'),
            bg='black',
            fg='white'
        )
        self.label3.place(x=380, y=80)
        self.main_text = Listbox(
            self.root,
            height=13,
            bd=5,
            width=26,
            font="Helvetica 16 italic bold"
        )
        self.main_text.place(x=300, y=140)
        self.text = Text(
            self.root,
            bd=5,
            height=2,
            width=20,
            font='Helvetica 16 bold'
        )
        self.text.place(x=30, y=150)

        
        def add():
            content = self.text.get(1.0, END).strip()  
            if content:  
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')  
                self.text.delete(1.0, END)

        
        def delete():
            delete_ = self.main_text.curselection()
            if delete_:  
                index = delete_[0]  
                look = self.main_text.get(index)

                with open('data.txt', 'r+') as f:
                    lines = f.readlines()  
                    f.seek(0)  
                    for line in lines:
                        if line.strip() != look: 
                            f.write(line)
                    f.truncate()  

                self.main_text.delete(index)  

        
        if os.path.exists('data.txt'):  
            with open('data.txt', 'r') as file:
                read = file.readlines()
                for i in read:
                    self.main_text.insert(END, i.strip())  

        
        self.button = Button(
            self.root,
            text="Add",
            font='Helvetica 16 bold italic',
            width=10,
            bd=5,
            bg='black',
            fg='white',
            command=add
        )
        self.button.place(x=30, y=230)
        
        self.button2 = Button(
            self.root,
            text="Delete",
            font='Helvetica 16 bold italic',
            width=10,
            bd=5,
            bg='black',
            fg='white',
            command=delete
        )
        self.button2.place(x=30, y=310)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
