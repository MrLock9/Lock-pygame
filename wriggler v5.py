import pygame

pygame.init()


window = pygame.display.set_mode((300, 300))

clock = pygame.time.Clock()

# game audio system, loads audio file and loops it 100 times
pygame.mixer.init()
pygame.mixer.music.load('SFX/playlist.ogg')
pygame.mixer.music.play(loops=100, fade_ms=1500)

# draws player controlled platform
rect = pygame.Rect(0, 0, 40, 14)
rect.midbottom = window.get_rect().midbottom

county = 1
countx = 1
player_vel = 5
brick_width = 30
brick_height = 10
offset = 5



brick = pygame.Rect(0, 0, brick_width, brick_height)
brick.center = window.get_rect().center

class rectangles:
    brick_width = 30
    brick_height = 10
    def __init__(self, brick_width, brick_height, offsetx, offsety):
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.offsetx = offsetx
        self.offsety = offsety
    
    def rectsx(self):
        return self.brick_width
    def rectsy(self):
        return self.brick_height


rect1 = pygame.Rect(0, 0, brick_width, brick_height)

while county <= 4:
    while countx <= 6:
        rect1.topleft = (5, 5)
        pygame.draw.rect(window, (220, 30, 250), rect1)
        countx = countx + 1
    county = county + 1

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
    
    #create offset variable, use original toplfet square, add an offset



    # controls the horizontal movement of the player, change vel value outside of the loop for faster controlling
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_vel

    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, (220, 30, 250), brick)
    pygame.draw.rect(window, (255, 90, 0), rect)
    pygame.display.flip()

    pygame.draw.rect(window, (200, 20, 20), rect1)

pygame.quit()
exit()