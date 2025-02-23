import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize split angle
        new_angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(new_angle)
        v2 = self.velocity.rotate(-new_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = v1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = v2 * 1.2
        