import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS, color = "white"):
        super().__init__(x, y, radius)
        self.color = color

    def get_position_coordinate(self):
        return (self.position.x, self.position.y)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(surface=screen, color=self.color, center=self.get_position_coordinate() , radius=self.radius, width=2)
