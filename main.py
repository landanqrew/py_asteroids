import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock: pygame.time.Clock = pygame.time.Clock()
    # delta time
    dt: int = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate Groups
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()

    # Assign objects to groups
    group_updatable.add(player)
    group_drawable.add(player)

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        # update updatables
        group_updatable.update(dt)

        # move player based on key inputs
        player.move(dt)

        # iterate over drawables and apply the draw method individually
        for drawable in group_drawable:
            drawable.draw(screen)

        # call last
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
