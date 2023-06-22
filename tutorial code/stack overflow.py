# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:46:07 2018

@author: daniel
"""

import pygame
import sys
pygame.init()

# Setup the main display
display_width = 600
display_height = 600
display_res = (display_width, display_height)
display = pygame.display.set_mode(display_res)
display_color = (0, 0, 0)
display.fill(display_color)

# Setup the player controlled rectangle
player_width = 100
player_height = 20
player_size = (player_width, player_height)
player_surface = pygame.Surface(player_size)
player_rect = player_surface.get_rect()
rect_speed = 1
player_rect.x = 300
player_rect.y = display_height-50
player_color = (255, 255, 255)
player_surface.fill(player_color)

# Setup the bouncing ball
ball = pygame.image.load("BreakoutBall.jpg")
ball_rect = ball.get_rect()
ball_rect.y = 400
ball_speed = [1, 1]

# Setup the target blocks
target_width = 50
target_height = 20
target_size = (target_width, target_height)
x_offs = 10
y_offs = 10
n_rows = 5
target_color = (0,255,0)
target_surf_list = []
target_rect_list = []
for target_col in range(int(display_width / (target_width+x_offs))):
    for target_row in range(n_rows):
        target_surf = pygame.Surface(target_size)
        target_rect = target_surf.get_rect()
        x_location = x_offs + x_offs * target_col + target_width * target_col
        y_location = y_offs + y_offs * target_row + target_height * target_row
        target_rect.x = x_location
        target_rect.y = y_location
        target_surf.fill(target_color)
        target_surf_list.append(target_surf)
        target_rect_list.append(target_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect = player_rect.move([-rect_speed, 0])
    if keys[pygame.K_d]:
        player_rect = player_rect.move([rect_speed, 0])

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > display_width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > display_height:
        ball_speed[1] = -ball_speed[1]

    if player_rect.colliderect(ball_rect):
        ball_speed[1] = -ball_speed[1]

    for idx, x in enumerate(target_rect_list):
        if x.colliderect(ball_rect):
            del target_rect_list[idx]
            del target_surf_list[idx]
            ball_speed[1] = -ball_speed[1]
    display.fill(display_color)
    display.blit(player_surface, player_rect)
    display.blit(ball, ball_rect)
    for x in range(len(target_surf_list)):
        display.blit(target_surf_list[x], target_rect_list[x])
    pygame.display.flip()