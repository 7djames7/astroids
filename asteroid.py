import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        # Remove asteroid
        self.kill()

        # If small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: # If large enough to split
            # New asteroids properties
            angle = random.uniform(20,50)
            split1_v = self.velocity.rotate(angle)
            split2_v = self.velocity.rotate(-1*angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS

            # Generate new asteroids
            split1 = Asteroid(self.position.x, self.position.y, split_radius)
            split2 = Asteroid(self.position.x, self.position.y, split_radius)
            split1.velocity = split1_v * 1.2
            split2.velocity = split2_v * 1.2