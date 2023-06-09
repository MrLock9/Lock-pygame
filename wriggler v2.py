# pygame.key module
# https://www.pygame.org/docs/ref/key.html
#
# How to get keyboard input in pygame?
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842
#
# How can I make a sprite move when key is held down
# https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down/64611463#64611463
#
# How to get if a key is pressed pygame
# https://stackoverflow.com/questions/59830738/how-to-get-if-a-key-is-pressed-pygame/59831073#59831073
#
# GitHub - PyGameExamplesAndAnswers - Keys and keyboard events - Keys
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_keys_and_keyboard_event.md 
#
# https://replit.com/@Rabbid76/PyGame-ContinuousMovement

import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pygame.mixer.init()

pygame.mixer.music.load('SFX/playlist.ogg')
rect = pygame.Rect(0, 0, 40, 14)
rect.midbottom = window.get_rect().midbottom
vel = 5

brick = pygame.Rect(0, 0, 30, 10)
brick.center = window.get_rect().center

# def bricks(brick, window):
#     brick = pygame.Rect(0, 0, 30, 10)
#     brick.center = window.get_rect().center
    
#     return brick

pygame.mixer.music.play(loops=100, fade_ms=1500)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    # rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel

    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, (220, 30, 250), brick)
    pygame.draw.rect(window, (255, 90, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()