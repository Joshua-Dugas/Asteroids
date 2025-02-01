import pygame

from Asteroids.player import Player
from constants import *
from pygame.time import Clock

from constants import *


import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatables, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        screen.fill("black")
        updatables.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()