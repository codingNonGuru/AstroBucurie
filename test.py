import pygame
import math
from vector import *

screenSize = Vector(1000, 600)

GRAVITATIONAL_CONSTANT = 100.0

pygame.init()

screen = pygame.display.set_mode((screenSize.x, screenSize.y), pygame.DOUBLEBUF)

class Body:
    def __init__(self, position, impulse, mass):
        self.position = position
        self.velocity = impulse / mass
        self.mass = mass
        self.size = math.sqrt(mass) * 2.0

    def calculateAttraction (self, other):
        direction = other.position - self.position 
        distance = direction.getLength()
        
        gravitationalFactor = GRAVITATIONAL_CONSTANT / (distance ** 3)
        gravitationalFactor *= other.mass
        
        self.velocity += direction * gravitationalFactor 
        
    def updatePosition (self):
        self.position += self.velocity

    def draw (self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.size), 0)

        
sattelite = Body(screenSize / 4.0, Vector(4.5, -4.5), 1.0)
attractor = Body(screenSize / 2.0, Vector(0.0, 0.0), 200.0)

bodies = []

bodies.append(sattelite)
bodies.append(attractor)

newBody = Body(screenSize / 3.0, Vector(4.0, -4.0), 1.0)
bodies.append(newBody)

newBody = Body(screenSize / 5.0, Vector(5.0, -5.0), 1.0)
bodies.append(newBody)

while True:
    screen.fill((0, 0, 0))

    for body in bodies:
        for otherBody in bodies:
            if body is not otherBody:
                body.calculateAttraction(otherBody)

    for body in bodies:
        body.updatePosition()

    for body in bodies:
        body.draw()
    
    pygame.display.flip()
