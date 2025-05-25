import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int, color: str = "white"):
        super().__init__(x, y, radius)
        self.color: str = color
        self.x = x
        self.y = y
        # self.radius = radius
        # self.speed: int = speed
        #self.velocity: pygame.Vector2 = super().velocity

    def get_position_coordinate(self):
        return (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=self.color, center=self.get_position_coordinate() , radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt