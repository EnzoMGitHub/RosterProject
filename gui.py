from tkinter import *
from PIL import Image, ImageTk
import os



class gui():

    def __init__(self):

        root = Tk()

        image_path = ['/Users/enzom/code/Github_Private_Projects/RosterProject/Screenshot 2024-02-22 at 8.38.51 PM copy.png']

        def billsClick(event):
            print("All good")

        root.minsize(height=600,width=800)
        frame = Frame(root,bg='light blue')
        frame.pack(expand=YES, fill=BOTH)

        title = Label(frame, text='Select a Team to Begin', bg='light blue', fg='black', font=('Arial', 20))
        title.pack(side=TOP)

        # photo = PhotoImage(file='/Users/enzom/code/Github_Private_Projects/RosterProject/Screenshot 2024-02-22 at 8.38.51 PM copy.png')
        # button = Button(frame, image=photo, compound=LEFT,bg='light blue')
        # button.pack()

        canvas = Canvas(frame, width=300, height=300, bg='light blue')
        canvas.pack()   

        directory = os.path.join('/Users/enzom/code/Github_Private_Projects/RosterProject','bills.png')
        button_image = Image.open(directory)
        bills = Button(root,image=button_image) 
        button_photo = ImageTk.PhotoImage(button_image)

        button = canvas.create_image(50, 50, image=button_photo, anchor=NW)
        canvas.tag_bind(button, "<Button-1>", billsClick)

    def clean():
        pass

gui()
mainloop()