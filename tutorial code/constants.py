import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]
ball_radius = 10
ball_color = [222,50,50]
ball_speed_x = 3
ball_speed_y = 5
ball_y = 100
ball_x = 100
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 10
class Brick(pygame.sprite.Sprite):
    image = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        if Brick.image is None:
            # This is the first time this class has been instantiated. So, load the image
            Brick.image = pygame.image.load("graphics/download.jpg")
        self.image = Brick.image

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)
brick_array = []
for i in range(1,8):
    brick1 = Brick(75*i,50)
    brick_array.append(brick1)
running = True
while running:
    for event in pygame.event.get():
        # Check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # Move the paddle based on mouse movement
            coordinates = pygame.mouse.get_pos()
            paddle_x = coordinates[0] - paddle_width/2
            paddle_y = coordinates[0] - paddle_height/2
            if paddle_x < 0:
                paddle_x = 0
            if paddle_x > screen.get_width() - paddle_width:
                paddle_x = screen.get_width() - paddle_width
    # Move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    
    # Check if the ball is off the bottom of the screen
    if ball_y > screen.get_height() - ball_radius:
        ball_speed_y = -ball_speed_y
    
    # Check if the ball hit the top of the screen
    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    
    # Check if the ball hit the left side of the screen
    if ball_x < ball_radius:
        ball_speed_x = -ball_speed_x
    
    # Check if the ball hit the right side of the screen
    if ball_x > screen.get_width() - ball_radius:
        ball_speed_x = -ball_speed_x

    # Create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    
    # Check for collisions with bricks
    for brick in brick_array:
        if brick.rect.colliderect(ball_rect):
            score = score + 1
            brick_array.remove(brick)
            ball_speed_y = - ball_speed_y
    
    # Check for collision with paddle
    if ball_rect.colliderect(paddle_rect):
        ball_speed_y = -ball_speed_y
    # Clear the screen
    screen.fill(black)

    # Draw the bricks
    for brick in brick_array:
        screen.blit(brick.image, brick.rect)
    
    # Draw the ball
    pygame.draw.circle(screen, ball_color, [int(ball_x), int(ball_y)], ball_radius, 0)
    
    # Draw the paddle
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    
    # Update the display
    pygame.display.update()
pygame.quit()
