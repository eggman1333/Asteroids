# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player  # Make sure you have a player.py file with a Player class

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Instantiate Player at screen center
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        player.draw(screen) # Draw the player
        player.update(dt)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
