import pygame

pygame.init()
width = 300
height = 300

window = pygame.display.set_mode((300, 300))

clock = pygame.time.Clock()

# game audio system, loads audio file and loops it 100 times
pygame.mixer.init()
pygame.mixer.music.load('SFX/playlist.ogg')
pygame.mixer.music.play(loops=100, fade_ms=1500)

# draws player controlled platform
rect = pygame.Rect(0, 0, 40, 14)
rect.midbottom = window.get_rect().midbottom

countx = 1
county = 1
player_vel = 5
brick_width = 30
brick_height = 10
offset = 5
brick_width = 30
brick_height = 10

brick = pygame.Rect(0, 0, brick_width, brick_height)
brick.center = window.get_rect().center

def drawrects(x, y, width, height, color):
    pygame.draw.rect(window, color, (x, y, width, height))

# rect1 = pygame.Rect(0, 0, brick_width, brick_height)
#create offset variable, use original toplfet square, add an offset

# for row in range(3):
#     for column in range(3):
#         rect_x = column * width
#         rect_y = row * height
#         rect_width = width // 3
#         rect_height = height // 3
#         color = (255, 0, 0) if (row + column) % 2 == 0 else (0, 255, 0)
#         draw_rectangle(rect_x, rect_y, rect_width, rect_height, color)
while county <= 4:
    while countx <= 6:
        print("Good")
        rect_x = countx * width
        rect_y = county * height
        rect_width = width / 3
        rect_height = height / 3
        color = (255, 0, 0)
        drawrects(rect_x, rect_y, rect_width, rect_height, color)
        countx = countx + 1
    print("County increased")
    county = county + 1
pygame.display.flip()

run = True
while run:
    # makes the game refresh 60 times per second
    clock.tick(60)

    # closes the game when closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.KEYDOWN:
        #     print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    



    # controls the horizontal movement of the player, change vel value outside of the loop for faster controlling
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_vel

    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    # window.fill(0)
    pygame.draw.rect(window, (220, 30, 250), brick)
    pygame.draw.rect(window, (255, 90, 0), rect)
    pygame.display.flip()



pygame.quit()
exit()