import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Atari Breakout")

# Set up the colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the paddle
paddle_width, paddle_height = 75, 15
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10
paddle_speed = 5

# Set up the ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = 3

# Set up the blocks
block_width, block_height = 60, 20
num_blocks = 5
blocks = []
for i in range(num_blocks):
    block_x = i * (block_width + 10) + 50
    block_y = 50
    blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_x > screen_width - ball_radius or ball_x < ball_radius:
        ball_speed_x *= -1
    if ball_y < ball_radius:
        ball_speed_y *= -1
    if ball_y > screen_height - ball_radius:
        # Game over
        running = False
    
    if paddle_y - ball_radius < ball_y < paddle_y and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y *= -1
    
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_speed_y *= -1
    
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()