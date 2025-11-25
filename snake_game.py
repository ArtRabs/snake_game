import pygame

pygame.init()

# Screen setup
WIDTH = 600     # Width of the screen in pixels
HEIGHT = 400    # Height of the screen in pixels

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen
pygame.display.set_caption("Snake Game")  # Set the title of the window