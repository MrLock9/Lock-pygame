import pygame
import math
pygame.init()
width = 512
height = 500


# Define constants for the colors of the bricks
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
player_vel = 5
rows = 6
columns = 8

window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# game audio system, loads audio file and loops it 100 times
pygame.mixer.init()
pygame.mixer.music.load('SFX/playlist.ogg')
pygame.mixer.music.play(loops=100, fade_ms=1500)

# draws player controlled platform
player = pygame.Rect(0, 0, 40, 14)
player.midbottom = window.get_rect().midbottom

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()



#Create a list to hold the bricks
bricks = pygame.sprite.Group()

# Create the bricks and add them to the list
for row in range(rows):
    for column in range(columns):
        if row < 2:
            brick = Brick(YELLOW, 60, 20)
        elif row < 4:
            brick = Brick(GREEN, 60, 20)
        elif row < 6:
            brick = Brick(ORANGE, 60, 20)
        else:
            brick = Brick(RED, 60, 20)
        brick.rect.x = column * 64
        brick.rect.y = row * 24
        bricks.add(brick)




run = True
while run:
    # makes the game refresh 60 times per second
    clock.tick(60)

    # closes the game when closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # controls the horizontal movement of the player, change vel value outside of the loop for faster controlling
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_vel

    player.centerx = player.centerx % window.get_width()
    player.centery = player.centery % window.get_height()
    # Display the bricks on the screen
    for brick in bricks:
        window.blit(brick.image, brick.rect)

    pygame.draw.rect(window, (255, 90, 0), player)
    pygame.display.flip()
    window.fill(0)
pygame.quit()
exit()