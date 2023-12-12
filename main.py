# pylint: disable=no-member
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption('Dolphin Survivors')

# Game loop flag
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()