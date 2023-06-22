"""
Atari Breakout in Pygame - Incomplete
Designed by Lachlan Mayne 2023
Packages required : pygame and random
Files required : main.py and ball.py and music.ogg
"""

# imports and initialises pygame
import pygame
pygame.init()
from ball import Ball

# defines the screen size
width = 512
height = 500

# Define constants for the colours of the bricks
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# defines the velocity of the player controlled platform
player_vel = 5

# defines the amount of rows and columns for the bricks
rows = 6
columns = 8

ball_sprite = pygame.sprite.Group()

# defines the game window
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# game audio system, loads audio file and loops it 100 times
pygame.mixer.init()
pygame.mixer.music.load('SFX/music.ogg')
pygame.mixer.music.play(loops=100, fade_ms=1500)

# draws player controlled platform
player = pygame.Rect(0, 0, 40, 14)
player.midbottom = window.get_rect().midbottom

# defines a class for the bricks
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

#Create the ball sprite
ball = Ball((255, 255, 255),10,10)
ball.rect.x = 345
ball.rect.y = 195
ball_sprite.add(ball)

# main game loop
run = True
while run:
    # makes the game refresh 60 times per second
    clock.tick(60)

    # closes the game when closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # updates the ball sprite, and checks for any keys pressed
    ball_sprite.update()
    keys = pygame.key.get_pressed()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=width:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>height:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
    
    # controls the horizontal movement of the player, change vel value outside of the loop for faster controlling
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_vel
    
    # Display the bricks on the screen
    for brick in bricks:
        window.blit(brick.image, brick.rect)
    
    # draws the ball sprite, the player sprite, and refreshes the screen
    ball_sprite.draw(window)
    pygame.draw.rect(window, (255, 90, 0), player)
    pygame.display.flip()
    window.fill(0)
pygame.quit()
exit()