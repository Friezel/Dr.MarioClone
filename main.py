#Inporteren van pygame
import pygame

#Initialiseren van pygame
pygame.init()

#Schermgrootte & scherm aanmaken
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#player aanmaken (rood vierkant)
player=pygame.image.load('../sprites/blok rood geel.png').convert()

#De run variabele
run = True

x=0

#Gameloop
while(run==True):
    #Zet scherm in het zwart
    screen.fill((0,0,0))
    
    #Tekend het vierkant
    screen.blit(player,(x,30))

    #Maakt het mogelijk om vierkant te bewegen
    key=pygame.key.get_pressed()
    if(key[pygame.K_q]==True):
        player.move_ip(-1,0)
    elif(key[pygame.K_d]==True):
        player.move_ip(1,0)
    elif(key[pygame.K_z]==True):
        player.move_ip(0,-1)
    elif(key[pygame.K_s]==True):
        player.move_ip(0,1)

    #Event checker die nakijkt of er op de x is gedrukt om het programma uit te zetten
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    #Refrech het display
    pygame.display.update()
#Zet pygame uit nadat de loop uit is
pygame.quit