import pygame
from constants import *
from player import Player  # Make sure you have a player.py file with a Player class
from asteroid import Asteroid  # Make sure you have an asteroid.py file with an Asteroid class
from asteroidfield import AsteroidField  # Make sure you have an asteroidfield.py file with an AsteroidField class

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable_sprites = pygame.sprite.Group()
    drawable_sprites = pygame.sprite.Group()
    asteroid_sprites = pygame.sprite.Group()
    
    Player.containers = (updateable_sprites, drawable_sprites)
    Asteroid.containers = (updateable_sprites, drawable_sprites, asteroid_sprites)
    AsteroidField.containers = (updateable_sprites)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Instantiate Player at screen center
    asteroid_field = AsteroidField()  # Instantiate AsteroidField

    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updateable_sprites.update(dt)

        screen.fill("black")
        
        for obj in drawable_sprites:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
