import pygame, sys

pygame.init()

# Screen setup
WIDTH = 600     # Width of the screen in pixels
HEIGHT = 400    # Height of the screen in pixels

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen
pygame.display.set_caption("Snake Game")  # Set the title of the window

clock = pygame.time.Clock() # Clock for controlling frame rate

while True:  # Main game loop

    for event in pygame.event.get():  # Event loop

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill the screen with black

    pygame.display.flip()  # Refresh display

    clock.tick(10) # Control speed (frames per second) in this case 10 FPS