
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

# Set score + get topscore
points = 0
score = 0
removed = 0
lost = 1
try: 
    with open ("topscore.txt", "r") as f:
        topscore = int(f.read())
except FileNotFoundError:
    topscore = 0

# Events
MOVEDOWN=pygame.USEREVENT+1
movedownInterval=500
pygame.time.set_timer(MOVEDOWN,movedownInterval)

# Font en letters
font=pygame.font.Font("Fonts/PixelifySans-VariableFont_wght.ttf",50)

# Status variabelen
home = True
run = False
pause = False
game_over = False

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

# Play screen
stop = font.render('STOP',False,'Red')
stop_rect = stop.get_rect(center = (700,50))

pause_button = font.render('PAUSE',False,'Red')
pause_button_rect = pause_button.get_rect(center = (400,50))

# Pause screen
paused = font.render('Paused',False,'White')
paused = pygame.transform.rotozoom(paused,0,2)
paused_rect = paused.get_rect(center = (400,150))

cont = font.render('Press space to continue',False,'White')
cont_rect = cont.get_rect(center = (400,500))

# Game Over screen
gameover = font.render('GAME OVER',False,'Red')
gameover = pygame.transform.rotozoom(gameover,0,2)
gameover_rect = gameover.get_rect(center = (400,150))

play = font.render('Press space to play again',False,'White')
play_rect = play.get_rect(center = (400,500))

home_button = font.render('Home',False,'White')
home_button_rect = home_button.get_rect(center = (100,50))

# Gameloop
while(True):
    # Event Handeler
    for event in pygame.event.get():

        # Quit
        if event.type==pygame.QUIT:
            with open("topscore.txt", "w") as f:
                f.write(str(topscore))
            pygame.quit()
            exit()

        # Click actions
        if event.type==pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                run=True
                home=False
            if stop_rect.collidepoint(event.pos):
                home=True
                run=False
                Functions.clearGrid(grid)
            if pause_button_rect.collidepoint(event.pos):
                pause=True
                run=False
            if home_button_rect.collidepoint(event.pos):
                home=True
                game_over=False
                Functions.clearGrid(grid)
                
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
            if event.key==pygame.K_SPACE and home == True:
                run=True
                home=False
                Functions.clearGrid(grid)
            if event.key==pygame.K_SPACE and game_over == True:
                run=True 
                game_over=False
                Functions.clearGrid(grid)
            if event.key==pygame.K_SPACE and pause == True:
                run=True
                pause=False

        # Eventtimer die blokje doet vallen
        if event.type==MOVEDOWN and run == True:
            if(Functions.detectblok(grid,player)!=True):
                player=Functions.moveObject(grid,"South",player)

        # Spawner van nieuw blokje nadat oude gevallen is
        if(Functions.detectblok(grid,player)==True):
            lost=Functions.height(grid)
            removed = Functions.countblok(grid)
            if removed > 0:
                Functions.gravity(grid)
                score += (removed*10)
                removed=0
            Functions.spawn(grid)
            player=Functions.vindObject(grid)
            
    if lost == 0:
        game_over=True
        run=False
        lost = 1

    #Score
    if score > topscore: topscore = score

    
        
    # Define score text
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

    #State functions
    if run == True:
        screen.fill((0,0,0))
        Functions.maakGrid(grid,screen,PLAYAREA_HEIGHT,PLAYAREA_WIDTH)

        # Decorations
        mario_rect.midbottom = (600,425)
        screen.blit(mario,mario_rect)
        pygame.draw.rect(screen,'Beige',pygame.Rect(50,50,150,200))

        # Pause and Stop
        screen.blit(stop,stop_rect)
        screen.blit(pause_button,pause_button_rect)

        # Score Display
        screen.blit(score_message,score_message_rect)
        screen.blit(score_number,score_number_rect)
        screen.blit(top_message,top_message_rect)
        screen.blit(top_number,top_number_rect)

    elif home == True: 
        screen.fill((94,129,162))
        screen.blit(mario,mario_rect)
        screen.blit(text,text_rect)
        screen.blit(start_surf,start_rect)

        top_message = font.render('Top:',False,(111,196,169))
        top_message_rect = top_message.get_rect(center = (150,260))
        screen.blit(top_message,top_message_rect)
        top_number = font.render(f'{topscore}',False,(111,196,169))
        top_number_rect = top_number.get_rect(center = (150,320))
        screen.blit(top_number,top_number_rect)

    elif pause == True:
        screen.fill('Black')
        screen.blit(paused,paused_rect)
        screen.blit(cont,cont_rect)
    
    elif game_over == True:
        screen.fill('Black')
        screen.blit(gameover,gameover_rect)
        screen.blit(home_button,home_button_rect)

        score_message = font.render('Your score:',False,'White')
        score_message_rect = score_message.get_rect(midbottom = (400,320))
        screen.blit(score_message,score_message_rect)

        score_number = font.render(f'{score}',False,'White')
        score_number_rect = score_number.get_rect(midbottom = (400,390))
        screen.blit(score_number,score_number_rect)

        screen.blit(play,play_rect)

    # Refresh het display + clocktick
    pygame.display.update()
    clock.tick(60)