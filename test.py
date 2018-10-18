import pygame
import math
from vector import *

screenSize = Vector(1000, 600)

GRAVITATIONAL_CONSTANT = 2000.0

pygame.init()

screen = pygame.display.set_mode((screenSize.x, screenSize.y), pygame.DOUBLEBUF)

class Body:
    def __init__(self, position, impulse, mass):
        self.position = position
        self.velocity = impulse / mass
        self.mass = mass

    def calculateAttraction (self, other):
        direction = other.position - self.position 
        distance = direction.getLength()
        
        gravitationalFactor = GRAVITATIONAL_CONSTANT / (distance ** 3)
        gravitationalFactor *= other.mass
        
        self.velocity += direction * gravitationalFactor 
        
    def updatePosition (self):
        self.position += self.velocity

    def draw (self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), 2, 0)

        
sattelite = Body(screenSize / 3.5, Vector(5.0, -5.0), 1.0)
attractor = Body(screenSize / 1.5, Vector(-5.0, 5.0), 20.0)

while True:
    screen.fill((0, 0, 0))

    sattelite.calculateAttraction(attractor)
    attractor.calculateAttraction(sattelite)

    sattelite.updatePosition()
    attractor.updatePosition()

    sattelite.draw()
    attractor.draw()
    
    pygame.display.flip()
