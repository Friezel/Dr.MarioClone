
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
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Opzetten van clockset
clock=pygame.time.Clock()

#vars
bottom=419
speed=1
start=200
edgeleft=208

#font en letters
font=pygame.font.Font("./Python/Pygame/Dr.MarioClone/Fonts/PixelifySans-VariableFont_wght.ttf",50)

#De run variabele
run = True

#static
background=pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/background.png").convert()
kader=pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/kader.png")
kader_rect=kader.get_rect(midbottom=(300,600))
text_surface=font.render("Score",False,"White")

#moving
blok_geel_rood= pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/blokroodgeel.png")
blok_rect=blok_geel_rood.get_rect(midbottom=(300,200))

#Gameloop
while(run==True):
    #Event Handeler
    for event in pygame.event.get():
        #quit
        if event.type==pygame.QUIT:
            run = False
        #controls
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if(blok_rect.x!=351):
                    blok_rect.x+=1
            if event.key==pygame.K_LEFT:
                if(blok_rect.x!=edgeleft):
                    blok_rect.x-=1
        
    Functions.maakGrid(10,10,screen)
       
    #print("x="+str(blok_rect.x)+" y="+str(blok_rect.y))

    #init background sprites
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    screen.blit(kader,kader_rect)
    screen.blit(text_surface,(500,200))
    
    #init keys
    keys=pygame.key.get_pressed()

    #init moving sprites
    screen.blit(blok_geel_rood,blok_rect)
    #naarbeneden
    if(blok_rect.y!=bottom):
        blok_rect.y+=speed

    #Refrech het display + clocktick
    pygame.display.update()
    clock.tick(60)
#Zet pygame uit nadat de loop uit is
pygame.quit