import pygame
def initGrid():
    grid=[]
    for i in range(20):
        row=[]
        for j in range(10):
            row.append(0)
        grid.append(row)
    return grid
def vindObject(grid):
    loc=[]
    for i in range(20):
        for j in range(10):
            if(grid[i][j]==1):
                yx=[i,j]
                loc.append(yx)
    return loc
def moveObject(grid,dir):
    obj=vindObject(grid)
    eind=False
    if(dir=="East"):
        for i in range(len(obj)):
            if(obj[i][1]==9):
                eind=True
        if(eind==False):
            for i in reversed(obj):
                grid[i[0]][i[1]]=0
                grid[i[0]][i[1]+1]=1
    if(dir=="West"):
        for i in range(len(obj)):
            if(obj[i][1]==0):
                eind=True
        if(eind==False):
            for i in obj:
                grid[i[0]][i[1]]=0
                grid[i[0]][i[1]-1]=1
    if(dir=="North"):
        for i in range(len(obj)):
            if(obj[i][0]==0):
                eind=True
        if(eind==False):
            for i in obj:
                grid[i[0]][i[1]]=0
                grid[i[0]-1][i[1]]=1
    if(dir=="South"):
        for i in range(len(obj)):
            if(obj[i][0]==19):
                eind=True
        if(eind==False):
            for i in reversed(obj):
                grid[i[0]][i[1]]=0
                grid[i[0]+1][i[1]]=1
    
                

def maakGrid(grid,screen,startx,starty):
    telx=0
    tely=0
    x=startx
    y=starty
    WHITE=(200,200,200)
    RED=(255,0,0)
    blokgrootte=20
    width=10
    for i in range(0,len(grid)):
        for j in range(0,width):
            vierkant=pygame.Rect(x,y,blokgrootte,blokgrootte)
            if(grid[tely][telx]==0):
                pygame.draw.rect(screen,WHITE,vierkant,1)
            if(grid[tely][telx]==1):
                pygame.draw.rect(screen,RED,vierkant)
            x+=blokgrootte
            telx+=1
        x=startx
        telx=0
        tely+=1
        y+=blokgrootte