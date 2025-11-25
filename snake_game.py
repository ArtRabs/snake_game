import pygame, sys

pygame.init()

# Screen setup
WIDTH = 600     # Width of the screen in pixels
HEIGHT = 400    # Height of the screen in pixels
CELL_SIZE = 20  # Size of each cell in pixels

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen
pygame.display.set_caption("Snake Game")  # Set the title of the window

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake setup (just a few blocks to start)
snake = [(100, 100), (80, 100), (60, 100)] # starting body position
direction = (CELL_SIZE, 0) # moving right 20 pixels each frame

# Main game loop
while True:  
    # Event loop
    for event in pygame.event.get():  

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                direction = (0, -CELL_SIZE)

            elif event.key == pygame.K_DOWN:
                direction = (0, CELL_SIZE)

            elif event.key == pygame.K_LEFT:
                direction = (-CELL_SIZE, 0)

            elif event.key == pygame.K_RIGHT:
                direction = (CELL_SIZE, 0)

        # Move Snake
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head) # add new head
        snake.pop() # remove tail

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Refresh display
    pygame.display.flip()  
    clock.tick(10) # Control speed (frames per second) in this case 10 FPS