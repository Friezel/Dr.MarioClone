
# Inporteren van pygame
import pygame
import Functions
from sys import exit
from random import randint

# Initialiseren van pygame
pygame.init()

# Titel
pygame.display.set_caption('Dr.Mario Clone')

# Schermgrootte & scherm aanmaken
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Grid aanmaken en speelveld aanmaken
PLAYAREA_WIDTH=100
PLAYAREA_HEIGHT=240
grid=Functions.initGrid()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Opzetten van de clock
clock=pygame.time.Clock()

# Score
score = 0
topscore = 0
if score > topscore: topscore = score

# Events
MOVEDOWN=pygame.USEREVENT+1
movedownInterval=500
pygame.time.set_timer(MOVEDOWN,movedownInterval)

# Font en letters
font=pygame.font.Font("Fonts/PixelifySans-VariableFont_wght.ttf",50)

# De run variabele
run = False

# Eerste blokje spawnen en als player zetten
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

# Game screen
score_message = font.render('Your score:',False,'Black')
score_message = pygame.transform.rotozoom(score_message,0,0.4)
score_message_rect = score_message.get_rect(midbottom = (125,100))

score_number = font.render(f'{score}',False,'Black')
score_number = pygame.transform.rotozoom(score_number,0,0.4)
score_number_rect = score_number.get_rect(midbottom = (125,130))

top_message = font.render('Top:',False,'Black')
top_message = pygame.transform.rotozoom(top_message,0,0.4)
top_message_rect = top_message.get_rect(midbottom = (125,180))

top_number = font.render(f'{topscore}',False,'Black')
top_number = pygame.transform.rotozoom(top_number,0,0.4)
top_number_rect = top_number.get_rect(midbottom = (125,210))

# Gameloop
while(True):
    # Scherm tekenen
    screen.fill((0,0,0))
    Functions.maakGrid(grid,screen,PLAYAREA_HEIGHT,PLAYAREA_WIDTH)

    # Event Handeler
    for event in pygame.event.get():

        # Quit
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                run=True

        # Controls
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


        # Eventtimer die blokje doet vallen
        if event.type==MOVEDOWN:
            if(Functions.detectblok(grid,player)!=True):
                player=Functions.moveObject(grid,"South",player)

        # Spawner van nieuw blokje nadat oude gevallen is
        if(Functions.detectblok(grid,player)==True):
            Functions.countblok(grid)
            Functions.gravity(grid)
            Functions.spawn(grid)
            player=Functions.vindObject(grid)
    
    if run:
        screen.fill((0,0,0))
        Functions.maakGrid(grid,screen,PLAYAREA_HEIGHT, PLAYAREA_WIDTH)
        score = 0

        # Inkleding
        mario_rect.midbottom = (600,425)
        screen.blit(mario,mario_rect)

        pygame.draw.rect(screen,'Beige',pygame.Rect(50,50,150,200))
        screen.blit(score_message,score_message_rect)
        screen.blit(score_number,score_number_rect)
        screen.blit(top_message,top_message_rect)
        screen.blit(top_number,top_number_rect)

        # Score

    else: 
        screen.fill((94,129,162))
        screen.blit(mario,mario_rect)
        screen.blit(text,text_rect)
        screen.blit(start_surf,start_rect)

    # Refrech het display + clocktick
    pygame.display.update()
    clock.tick(60)
# Zet pygame uit nadat de loop uit is
pygame.quit