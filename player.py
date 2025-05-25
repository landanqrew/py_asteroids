from constants import *
from circleshape import CircleShape
from shot import *
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        # self.containers

    # in the player class
    def triangle(self):
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface, color: str = "white", line_width: int = 2):
        pygame.draw.polygon(screen, color, self.triangle(), line_width)

    def rotate(self, dt: int):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
            self.rotate(dt)

    def move(self, dt: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # print('space key identified')
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        


