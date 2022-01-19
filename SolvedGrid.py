import random
import copy

#grid = [[0 for x in range(9)] for j in range(9)]
#flag = False

def checkzeros(grid):
    for x in grid:
        if 0 in x:
            return False
    return True


def checkBox(grid,row,column,num):
    temp = []
    startx = 3*(row//3)
    starty = 3*(column//3)
    for i in range(3):
        for j in range(3):
            temp.append(grid[startx+i][starty+j])
    if num in temp:
        return False
    else:
        return True

def checkRow(grid,row,column,num):
    if num in grid[row]:
        return False
    else:
        return True

def checkColumn(grid,row,column,num):
    temp = []
    for i in range(9):
        temp.append(grid[i][column])
    if num in temp:
        return False
    else:
        return True

def fillgrid(grid):
    
    for i in range(9):
        for j in range(9):
            x = random.randint(1,9)
            if(checkBox(grid,i,j,x) and checkColumn(grid,i,j,x) and checkRow(grid,i,j,x)):
                grid[i][j] = x


def createGrid():
    grid = [[0 for i in range(9)] for j in range(9)]
    flag = False
    while(not flag):
        for i in range(500):
            fillgrid(grid)
        if checkzeros(grid):
            flag = True
        else:
            grid = [[0 for i in range(9)] for j in range(9)]
    return grid


difficulty = 1
def removeElements(grid):
    if difficulty == 1:
        for i in range(9):
            for j in range(3):
                x = random.randint(0,8)
                grid[i][x]='_'
    if difficulty == 2:
        for i in range(9):
            for j in range(4):
                x = random.randint(0,8)
                grid[i][x]='_'
    if difficulty == 3:
        for i in range(9):
            for j in range(6):
                x = random.randint(0,8)
                grid[i][x]='_' 
    for i in range(9):
        grid[i].insert(3,' | ')
        grid[i].insert(7,' | ')
    grid.insert(3,['-' for x in range(11)])
    grid.insert(7,['-' for x in range(11)])

    answer = copy.deepcopy(grid)
    
    for i in range(9):
        answer[i].insert(3,' | ')
        answer[i].insert(7,' | ')
    answer.insert(3,['-' for x in range(11)])
    answer.insert(7,['-' for x in range(11)]) 

    return answer

'''createGrid(grid)
answer = copy.deepcopy(grid)
removeElements(grid) '''







