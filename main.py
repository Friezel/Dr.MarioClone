
#Inporteren van pygame
import pygame
import Functions
from sys import exit

#Initialiseren van pygame
pygame.init()

#Titel
pygame.display.set_caption('Dr.Mario Clone')

#Schermgrootte & scherm aanmaken
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Grid aanmaken en speelveld aanmaken
PLAYAREA_WIDTH=100
PLAYAREA_HEIGHT=240
grid=Functions.initGrid()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Opzetten van de clock
clock=pygame.time.Clock()

#Events
MOVEDOWN=pygame.USEREVENT+1
movedownInterval=500
pygame.time.set_timer(MOVEDOWN,movedownInterval)

#font en letters
font=pygame.font.Font("Fonts/PixelifySans-VariableFont_wght.ttf",50)

#De run variabele
run = False

#Eerste blokje spawnen en als player zetten
Functions.spawn(grid)
player=Functions.vindObject(grid)

# Intro screen
mario = pygame.image.load('sprites/Dr.Mario_Pixel.png').convert_alpha()
mario = pygame.transform.rotozoom(mario,0,0.5)
mario_rect = mario.get_rect(center = (400,300))

text = font.render('Dr. Mario Clone',False,(111,196,169))
text_rect = text.get_rect(center = (400,100))

start_surf = font.render('START',False,(111,196,169))
start_rect = start_surf.get_rect(center = (400,500))

#Gameloop
while True:
    

    #Event Handeler
    for event in pygame.event.get():

        #Quit
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                run=True

        #Controls
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player=Functions.moveObject(grid,"West",player)
            if event.key==pygame.K_RIGHT:
                player=Functions.moveObject(grid,"East",player)
            if event.key==pygame.K_UP:
                player=Functions.moveObject(grid,"North",player)
            if event.key==pygame.K_DOWN:
                player=Functions.moveObject(grid,"South",player)
            if event.key==pygame.K_SPACE:
                run=True
    
        #Eventtimer die blokje doet vallen
        if event.type==MOVEDOWN:
            if(Functions.detectblok(grid,player)!=True):
                player=Functions.moveObject(grid,"South",player)
    
    #Spawner van nieuw blokje nadat oude gevallen is
    if(Functions.detectblok(grid,player)==True):
        Functions.countblok(grid)
        Functions.spawn(grid)
        player=Functions.vindObject(grid)
    
    if run:
        #Scherm tekenen
        screen.fill((0,0,0))
        Functions.maakGrid(grid,screen,PLAYAREA_HEIGHT,PLAYAREA_WIDTH)

    else:
        screen.fill((94,129,162))
        screen.blit(mario,mario_rect)
        screen.blit(text,text_rect)
        screen.blit(start_surf,start_rect)

    #Refrech het display + clocktick
    pygame.display.update()
    clock.tick(60)
#Zet pygame uit nadat de loop uit is
pygame.quit