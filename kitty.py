import pygame

pygame.init()

#game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
width = 400
height = 500
background = white
player = pygame.transform.scale(pygame.image.load ('kittyplayer.jpg'), (90, 70))
fps = 60
timer = pygame.time.Clock()


#game variables
player_x = 170
player_y = 400


#screen
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('caliGO')

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    pygame.display.flip()
pygame.quit()