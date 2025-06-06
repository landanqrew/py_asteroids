import pygame
import math
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    clock: pygame.time.Clock = pygame.time.Clock()
    # delta time
    dt: int = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate Groups
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    # Specify that objects will be instantiated within these groups:
    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    AsteroidField.containers = (group_updatable)
    Shot.containers = (group_updatable, group_drawable, group_shots)
    


    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate Asteroid Field
    asteroid_field = AsteroidField()


    # Assign objects to groups
    '''
    commenting these out because Player.containers ... takes care of this
    group_updatable.add(player)
    group_drawable.add(player)
    '''
    

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        # update updatables
        group_updatable.update(dt)

        # check collisions
        for asteroid in group_asteroids:
            if asteroid.check_collision(player):
                print('Game Over!')
                # pygame.display.quit()
                return
            else:
                for shot in group_shots:
                    if asteroid.check_collision(shot):
                        shot.kill()
                        if asteroid.radius * ASTEROID_DIVISION_RATE > ASTEROID_MIN_RADIUS:
                            rand_angle = random.uniform(20,50)
                            asteroid_field.spawn(math.floor(asteroid.radius * ASTEROID_DIVISION_RATE),asteroid.position, velocity=asteroid.velocity.rotate(rand_angle))
                            asteroid_field.spawn(math.floor(asteroid.radius * ASTEROID_DIVISION_RATE),asteroid.position, velocity=asteroid.velocity.rotate(-1*rand_angle))

                        asteroid.kill()
                        


        # move player based on key inputs
        player.move(dt)
        player.shoot()

        # iterate over drawables and apply the draw method individually
        for drawable in group_drawable:
            drawable.draw(screen)

        # call last
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
