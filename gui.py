from tkinter import *
from PIL import Image, ImageTk
import os
import math



class gui():

    def __init__(self):

        root = Tk()

        image_path = ['/Users/enzom/code/Github_Private_Projects/RosterProject/Screenshot 2024-02-22 at 8.38.51 PM copy.png']

        def billsClick(event):
            print("All good")

        root.minsize(height=600,width=800)
        frame = Frame(root,bg='light blue')
        frame.pack(fill=BOTH)

        title = Label(frame, text='Select a Team to Begin', bg='light blue', fg='black', font=('Arial', 20))
        title.grid(row=0,column=1)

        # photo = PhotoImage(file='/Users/enzom/code/Github_Private_Projects/RosterProject/Screenshot 2024-02-22 at 8.38.51 PM copy.png')
        # button = Button(frame, image=photo, compound=LEFT,bg='light blue')
        # button.pack()
        teams = ['Arizona Cardinals','Atlanta Falcons','Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears' ,'Cincinnati Bengals' ,'Cleveland Browns', \
                'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts' \
                , 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers', 'Los Angeles Rams', \
                 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Philadelphia Eagles' \
                , 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans Washington Commanders']
        count = 0
        button_Frame = Frame(root)
        button_Frame.grid
        for i in teams:
            Button(button_Frame,text=i).grid(row=math.floor(count/5), column=(count%5)+1)
            count += 1

    def clean():
        pass

gui()
mainloop()