import pygame
def initGrid():
    grid=[]
    for i in range(20):
        row=[]
        for j in range(10):
            row.append(0)
        grid.append(row)
    return grid
def getKleur(nummer):
    if(nummer==0):
        return "wit"
    if(nummer==1):
        return "rood"
    if(nummer==2):
        return "geel"
    if(nummer==3):
        return "blauw"
def vindObject(grid):
    loc=[]
    kleur=0
    for i in range(20):
        for j in range(10):
            if(grid[i][j]!=0):
                kleur=grid[i][j]
                yx=[i,j,kleur]
                loc.append(yx)
    return loc
def moveObject(grid,dir):
    obj=vindObject(grid)
    eind=False
    kleur=0
    if(dir=="East"):
        for i in range(len(obj)):
            if(obj[i][1]==9):
                eind=True
        if(eind==False):
            for i in reversed(obj):
                kleur=i[2]
                grid[i[0]][i[1]+1]=kleur
                grid[i[0]][i[1]]=0
    if(dir=="West"):
        for i in range(len(obj)):
            if(obj[i][1]==0):
                eind=True
        if(eind==False):
            for i in obj:
                kleur=i[2]
                grid[i[0]][i[1]]=0
                grid[i[0]][i[1]-1]=kleur
    if(dir=="North"):
        for i in range(len(obj)):
            if(obj[i][0]==0):
                eind=True
        if(eind==False):
            for i in obj:
                kleur=i[2]
                grid[i[0]][i[1]]=0
                grid[i[0]-1][i[1]]=kleur
    if(dir=="South"):
        for i in range(len(obj)):
            if(obj[i][0]==19):
                eind=True
        if(eind==False):
            for i in reversed(obj):
                kleur=i[2]
                grid[i[0]][i[1]]=0
                grid[i[0]+1][i[1]]=kleur
    
                

def maakGrid(grid,screen,startx,starty):
    telx=0
    tely=0
    x=startx
    y=starty
    WHITE=(200,200,200)
    RED=(255,0,0)
    YELLOW=(255,255,0)
    BLUE=(0,0,255)
    blokgrootte=20
    width=10
    for i in range(0,len(grid)):
        for j in range(0,width):
            vierkant=pygame.Rect(x,y,blokgrootte,blokgrootte)
            if(getKleur(grid[tely][telx])=="wit"):
                pygame.draw.rect(screen,WHITE,vierkant,1)
            elif(getKleur(grid[tely][telx])=="blauw"):
                pygame.draw.rect(screen,BLUE,vierkant)
            elif(getKleur(grid[tely][telx])=="rood"):
                pygame.draw.rect(screen,RED,vierkant)
            elif(getKleur(grid[tely][telx])=="geel"):
                pygame.draw.rect(screen,YELLOW,vierkant)
            
            x+=blokgrootte
            telx+=1
        x=startx
        telx=0
        tely+=1
        y+=blokgrootte