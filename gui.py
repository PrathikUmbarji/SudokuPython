from random import uniform
from tkinter import*
from typing import Collection

from SolvedGrid import*

answer = [[0 for x in range(9)] for j in range(9)]

root = Tk()
root.title("Sudoku")
root.configure(background='Pink')
root.geometry("500x500")



def startGame():
    board = createGrid()
    answer = removeElements(board)
    
    wind = Toplevel()
    wind.geometry("180x230")
    Cont1 = Frame(wind)
    for i in range(11):
        for j in range(11):
            if(board[i][j] != '_'):
                labeltemp = Label(Cont1,text = board[i][j],fg='Blue')
                labeltemp.grid(row=i,column=j)
            else:
                labeltemp = Entry(Cont1,width="2",bg='white')
                labeltemp.grid(row=i,column=j)
    Cont1.pack()
    Cont2 = Frame(wind)
    btans = Button(wind,text = 'Show Answers',command = showAns).pack()
    


def seteasy():
    difficulty = 1 

def setmed():
    difficulty = 2

def sethard():
    difficulty = 3    


def chooseDiff():
    wind3 = Toplevel()
    wind3.geometry("100x75")
    easy = Button(wind3,text="EASY",font=("Bahnschrift", 10),command=seteasy and wind3.destroy).pack()
    med = Button(wind3,text="MEDIUM",font=("Bahnschrift", 10),command=setmed and wind3.destroy).pack()
    hard = Button(wind3,text="HARD",font=("Bahnschrift", 10),command=sethard and wind3.destroy).pack()


'''def showAns():
    wind2 = Toplevel()
    for i in range(11):
        for j in range(11):
            labeltemp = Label(wind2,text = answer[i][j],fg='Green')
            labeltemp.grid(row=i,column=15+j)
'''




MainLabel = Label(root,text = 'MAIN MENU',font=("Bahnschrift", 40),fg='Red',bg='Pink',width=15).pack(padx=0,pady=100)

start_game = Button(root,text="New Game",font=("Century Gothic Bold",12),command=startGame,width = 15).pack()

diff = Button(root,text = "Choose Difficulty",font = ("Century Gothic Bold",12),width=15,command = chooseDiff).pack()


Quit = Button(root,text="Quit",font=("Century Gothic Bold",12),command=root.destroy).pack()




root.mainloop()