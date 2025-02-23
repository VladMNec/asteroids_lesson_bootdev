# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import constants file
from constants import *
# import player
import player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    fps = pygame.time.Clock()
    dt = 0
    player.Player.containers = (updatable, drawable)
    player_sprite = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        frames = fps.tick(60)
        dt = frames / 1000
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()