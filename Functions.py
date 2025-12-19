import pygame
import random

# Functie die Grid aanmaakt
def initGrid():
    grid=[]
    for i in range(20):
        row=[]
        for j in range(10):
            row.append(0)
        grid.append(row)
    return grid

# Functie die kleur returned van gegeven waarde
def getKleur(nummer):
    if(nummer==0):
        return "wit"
    if(nummer==1):
        return "rood"
    if(nummer==2):
        return "geel"
    if(nummer==3):
        return "blauw"

# Functie die zoekt naar een object (enkel eerste rij)
def vindObject(grid):
    loc=[]
    kleur=0
    for j in range(10):
        if(grid[0][j]!=0):
            kleur=grid[0][j]
            yx=[0,j,kleur]
            loc.append(yx)
    return loc

# Functie die de oriëntatie van een object teruggeeft
def getorient(obj):
    if(obj[0][1]!=obj[1][1]):
        return "H"
    else:
        return "V"

# Bewegen van een object naar een gegeven richting + draaien
def moveObject(grid,dir,obj):
    eind=False
    kleur=0
    nieuw_pos=[]
    if(dir=="East"):
        # Nog probleem met verschuiving
        for i in range(len(obj)):
            if(obj[i][1]==9):
                eind=True
                for i in obj:
                    nieuw_pos.append(i)
        if(eind==False):
            for i in reversed(obj):
                kleur=i[2]
                grid[i[0]][i[1]+1]=kleur
                item=[i[0],i[1]+1,i[2]]
                grid[i[0]][i[1]]=0
                nieuw_pos.insert(0,item)

    if(dir=="West"):
        # Nog probleem met verschuiving
        for i in range(len(obj)):
            if(obj[i][1]==0):
                eind=True
                for i in obj:
                    nieuw_pos.append(i)
        if(eind==False):
            for i in obj:
                kleur=i[2]
                grid[i[0]][i[1]]=0
                item=[i[0],i[1]-1,i[2]]
                grid[i[0]][i[1]-1]=kleur
                nieuw_pos.append(item)
    if(dir=="North"):
        for i in range(len(obj)):
            if(obj[i][0]==0):
                eind=True
                for i in obj:
                    nieuw_pos.append(i)
        if(eind==False):
            tel=0
            if(getorient(obj)=="H"):
                for i in obj:
                    if(tel==0):
                        kleur=i[2]
                        grid[i[0]][i[1]]=0
                        grid[i[0]-1][i[1]]=kleur
                        item=[i[0]-1,i[1],i[2]]
                        nieuw_pos.append(item)
                    if(tel==1):
                        kleur=i[2]
                        grid[i[0]][i[1]]=0
                        item=[i[0],i[1]-1,i[2]]
                        grid[i[0]][i[1]-1]=kleur
                        nieuw_pos.append(item)
                    tel+=1
            else:
                for i in obj:
                    if(tel==0):
                        kleur=i[2]
                        grid[i[0]][i[1]]=0
                        grid[i[0]+1][i[1]+1]=kleur
                        item=[i[0]+1,i[1]+1,i[2]]
                        nieuw_pos.append(item)
                    if(tel==1):
                        nieuw_pos.insert(0,i)
                    tel+=1
    if(dir=="South"):
        for i in range(len(obj)):
            if(obj[i][0]==19):
                eind=True
                for i in obj:
                    nieuw_pos.append(i)
        if(eind==False):
            for i in reversed(obj):
                kleur=i[2]
                grid[i[0]][i[1]]=0
                grid[i[0]+1][i[1]]=kleur
                item=[i[0]+1,i[1],i[2]]
                nieuw_pos.insert(0,item)

    return nieuw_pos

# Tekenen van het grid met kleuren       
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

# Functie die blokken detetecteerd onder object
def detectblok(grid,obj):
    detect=False
    if(getorient(obj)=="H"):
        for i in obj:
            if(i[0]<19):
                if(grid[i[0]+1][i[1]]!=0):
                    detect=True
            else:
                detect=True
    else:
        if(obj[1][0]<19):
            if(grid[obj[1][0]+1][obj[1][1]]!=0):
                detect=True
        else:
            detect=True
    return detect

# Functie die blok bovenaan doet spawnen
def spawn(grid):
    blok1=random.randint(1,3)
    blok2=random.randint(1,3)
    grid[0][4]=blok1
    grid[0][5]=blok2

# Functie die checkt of er ergens 4 blokjes van dezelfde kleur naast of op elkaar zijn
def countblok(grid):
    
    removed = 0
    for i in range(20):
        tel=0
        gevonden=[]
        for j in range(10):
            if(grid[i][j]!=0):
                if(tel==0):
                    temp=[i,j]
                    gevonden.append(temp)
                    tel+=1
                elif(0<tel):
                    if(grid[i][j]==grid[i][j-1]):
                        temp=[i,j]
                        gevonden.append(temp)
                        tel+=1
                    else:
                        gevonden.clear()
                        tel=0
            elif(tel>=4):
                for z in gevonden:
                    grid[z[0]][z[1]]=0
                    removed += 1
                tel=0
        if(tel>=4):
            for z in gevonden:
                    grid[z[0]][z[1]]=0
                    removed += 1
            tel=0 
    i=0
    for i in range(10):
        tel=0
        gevonden=[]
        for j in range(20):
            if(grid[j][i]!=0):
                if(tel==0):
                    temp=[j,i]
                    gevonden.append(temp)
                    tel+=1
                elif(0<tel):
                    if(grid[j][i]==grid[j-1][i]):
                        temp=[j,i]
                        gevonden.append(temp)
                        tel+=1
                    else:
                        gevonden.clear()
                        tel=0
            elif(tel>=4):
                for z in gevonden:
                    grid[z[0]][z[1]]=0
                    removed += 1
                tel=0
        if(tel>=4):
            for z in gevonden:
                    grid[z[0]][z[1]]=0
                    removed += 1
            tel=0
    return removed

# Functie die zorgt voor een zwaartekracht effect
def gravity(grid):
    gevallen=True
    while(gevallen==True):
        gevallen=False
        for j in range(18,-1,-1):
            for i in range(10):
                if(grid[j][i]!=0 and grid[j+1][i]==0):
                    if(i<9 and grid[j][i+1]!=0):
                        if(grid[j+1][i]==0 and grid[j+1][i+1]==0):
                            grid[j+1][i] = grid[j][i]
                            grid[j+1][i+1] = grid[j][i+1]
                            grid[j][i] = 0
                            grid[j][i+1] = 0
                            gevallen = True
                    elif(j<19 and grid[j+1][i]):
                        boven=j-1
                        if(boven>=0 and grid[boven][i]!=0):
                            grid[j+1][i]=grid[j][i]
                            grid[j][i]=0
                            gevallen=True
                    else:
                        grid[j+1][i]=grid[j][i]
                        grid[j][i]=0
                        gevallen=True
def height(grid):
    for i in range(10):
        tel=0
        gevonden=[]
        for j in range(20):
            if(grid[j][i]!=0):
                temp=[j,i]
                gevonden.append(temp)
                tel+=1
        if(tel>=19):
            return 0
    return 1
                

# Functie die het bord leeg maakt
def clearGrid(grid):
    for x in range(20):
        for y in range(10):
            grid[x][y] = 0