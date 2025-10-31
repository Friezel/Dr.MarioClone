
#Inporteren van pygame
import pygame
import Functions
#Initialiseren van pygame
pygame.init()

#titel
pygame.display.set_caption('Dr.Mario Clone')

#Schermgrootte & scherm aanmaken
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYAREA_WIDTH=100
PLAYAREA_HEIGHT=240
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Opzetten van clockset
clock=pygame.time.Clock()

#Events
MOVEDOWN=pygame.USEREVENT+1
movedownInterval=500
pygame.time.set_timer(MOVEDOWN,movedownInterval)

#font en letters
#font=pygame.font.Font("./Python/Pygame/Dr.MarioClone/Fonts/PixelifySans-VariableFont_wght.ttf",50)

#De run variabele
run = True

grid=Functions.initGrid()
grid[0][4]=3
grid[0][5]=2

#Gameloop
while(run==True):
    screen.fill((0,0,0))
    Functions.maakGrid(grid,screen,PLAYAREA_HEIGHT,PLAYAREA_WIDTH)
    #Event Handeler
    for event in pygame.event.get():
        #quit
        if event.type==pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                Functions.moveObject(grid,"West")
            if event.key==pygame.K_RIGHT:
                Functions.moveObject(grid,"East")
        if event.type==MOVEDOWN:
            Functions.moveObject(grid,"South")
    
    
    #Refrech het display + clocktick
    pygame.display.update()
    clock.tick(60)
#Zet pygame uit nadat de loop uit is
pygame.quit