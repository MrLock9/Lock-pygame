# imports pygame into the environment, initiates the package for pygame + audio
import pygame
import sys
# import time
pygame.init()
pygame.mixer.init()

# sets a maximum screen size
screen = pygame.display.set_mode((800,400))
# titles the pygame window
pygame.display.set_caption('Lachlans demo')

# allows a maximum framerate to be set
clock = pygame.time.Clock()

pygame.mixer.music.load('SFX/kaboom.ogg')
test_surface = pygame.image.load('graphics/download.jpg')

x = 1
y = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.key.get_pressed()

    # checks if a key has been pressed
        if event.type == pygame.KEYDOWN:
        
        # inside the if loop determines what key has been pressed
            if event.key == pygame.K_a:
                x = x - 1
            elif event.key == pygame.K_d:
                x = x + 1
            elif event.key == pygame.K_w:
                y = y - 1
            elif event.key == pygame.K_s:
                y = y + 1
    # blit == block image transfer
    screen.blit(test_surface,(x,y))
    # x = x + 1
    # if y > 217:
    #     pygame.mixer.music.play()
    #     time.sleep(5)
    #     pygame.quit()
    # else:
    #     y = y + 1
    # draw all our elements
    # update everything
    pygame.display.update()
    # sets the maximum framerate to 60 (while loop doesn't clock more than 60 times per second)
    clock.tick(60)
