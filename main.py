#Inporteren van pygame
import pygame
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

font=pygame.font.Font("./Python/Pygame/Dr.MarioClone/Fonts/PixelifySans-VariableFont_wght.ttf",50)

#De run variabele
run = True

blok_geel_rood= pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/blokroodgeel.png").convert()
background=pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/background.png").convert()
kader=pygame.image.load("./Python/Pygame/Dr.MarioClone/sprites/kader.png")
text_surface=font.render("Score",False,"White")

#Gameloop
while(run==True):
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    screen.blit(kader,(-100,0))
    screen.blit(text_surface,(500,200))

    #Event checker die nakijkt of er op de x is gedrukt om het programma uit te zetten
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    #Refrech het display
    pygame.display.update()

    clock.tick(60)
#Zet pygame uit nadat de loop uit is
pygame.quit