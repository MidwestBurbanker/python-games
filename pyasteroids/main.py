import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()
    playership = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for space_objects in drawable:
            space_objects.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
