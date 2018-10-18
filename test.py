import pygame
import math
from vector import *

screenSize = Vector(1000, 600)

GRAVITATIONAL_CONSTANT = 20000.0

pygame.init()

screen = pygame.display.set_mode((screenSize.x, screenSize.y), pygame.DOUBLEBUF)

#sattelitePosition = screenSize / 3.5

#satteliteVelocity = Vector (1.0, 0.0)

#attractorPosition = screenSize / 2.0

class Body:
    def __init__(self, position):
        self.position = position
        self.velocity = Vector (0.0, 0.0)

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def calculateAttraction (self, other):
        direction = other.position - self.position 
        distance = direction.getLength() 
        gravitationalFactor = GRAVITATIONAL_CONSTANT / (distance ** 3) 
        self.velocity += direction * gravitationalFactor 
        
    def updatePosition (self):
        self.position += self.velocity

    def draw (self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), 2, 0)

        
sattelite = Body(screenSize / 3.5, Vector(5.0, -5.0))
attractor = Body(screenSize / 2.0, Vector(-5.0, 5.0))

while True:
    screen.fill((0, 0, 0))

    sattelite.calculateAttraction(attractor)
    attractor.calculateAttraction(sattelite)

    sattelite.updatePosition()
    attractor.updatePosition()

    sattelite.draw()
    attractor.draw()
    

 #   direction = attractorPosition - sattelitePosition

 #   distance = direction.getLength()
 
 #   gravitationalFactor = gravitationalConstant / (distance ** 3)
    
 #   satteliteVelocity += direction * gravitationalFactor
 #   sattelitePosition += satteliteVelocity

 #   pygame.draw.circle(screen, (255, 255, 255), (int(sattelitePosition.x), int(sattelitePosition.y)), 2, 0)
 #   pygame.draw.circle(screen, (255, 255, 255), (int(attractorPosition.x), int(attractorPosition.y)), 5, 0)
    
    pygame.display.flip()
