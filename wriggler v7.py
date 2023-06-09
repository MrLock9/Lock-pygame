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

brick_width = 30
brick_height = 10

brick = pygame.Rect(0, 0, brick_width, brick_height)
brick.center = window.get_rect().center

def drawrects(x, y, width, height, color):
    pygame.draw.rect(window, color, (x, y, width, height))

# Setup the target blocks
# target_width = 50
# target_height = 20
# target_size = (target_width, target_height)
# x_offs = 10
# y_offs = 10
# n_rows = 5
# target_color = (0,255,0)
# target_surf_list = []
# target_rect_list = []
# for target_col in range(int(display_width / (target_width+x_offs))):
#     for target_row in range(n_rows):
#         target_surf = pygame.Surface(target_size)
#         target_rect = target_surf.get_rect()
#         x_location = x_offs + x_offs * target_col + target_width * target_col
#         y_location = y_offs + y_offs * target_row + target_height * target_row
#         target_rect.x = x_location
#         target_rect.y = y_location
#         target_surf.fill(target_color)
#         target_surf_list.append(target_surf)
#         target_rect_list.append(target_rect)

countx = 1
county = 1
player_vel = 5
offset = 5
brick_width = 30
brick_height = 10
brick_size = (brick_width, brick_height)

while county <= 4:
    while countx <= 6:
        print("Good")
        target_surf = pygame.Surface(brick_size)
        target_rect = target_surf.get_rect()
        x_location = offset * county + brick_width * countx
        y_location = offset + offset * countx + brick_height * county
        
#         target_rect.x = x_location
#         target_rect.y = y_location
#         target_surf.fill(target_color)
#         target_surf_list.append(target_surf)
#         target_rect_list.append(target_rect)
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