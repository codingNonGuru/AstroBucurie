import pygame
from pygame.locals import *
import math
from vector import *

screenSize = Vector(1000, 600)

GRAVITATIONAL_CONSTANT = 50.0

TIME_FACTOR = 0.05

SIZE_MASS_FACTOR = 1.0

TRAIL_SIZE = 1000

pygame.init()

screen = pygame.display.set_mode((screenSize.x, screenSize.y), pygame.DOUBLEBUF | pygame.FULLSCREEN)

class Body:
    def __init__(self, position, impulse, mass):
        self.position = position
        self.velocity = (impulse / mass) 
        self.mass = mass
        self.size = math.sqrt(mass) * SIZE_MASS_FACTOR

        self.pastPositions = []
        for x in range(0, TRAIL_SIZE):
            self.pastPositions.append(position)

        self.trailIndex = 0

    def calculateAttraction (self, other):
        direction = other.position - self.position 
        distance = direction.getLength()
        
        gravitationalFactor = GRAVITATIONAL_CONSTANT / (distance ** 3)
        gravitationalFactor *= other.mass
        
        self.velocity += direction * gravitationalFactor * TIME_FACTOR
        
    def updatePosition (self):
        self.pastPositions[self.trailIndex] = self.position
        self.trailIndex += 1
        if self.trailIndex == TRAIL_SIZE:
            self.trailIndex = 0
        
        self.position += self.velocity * TIME_FACTOR

    def draw (self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.size), 0)
        surface = pygame.Surface((10, 10), pygame.SRCALPHA)
        for x in range(0, TRAIL_SIZE):
            surface.fill((255, 0, 0, 0))
            pygame.draw.circle(surface, (255, 255, 255, 64), (5, 5), 1, 0)
            screen.blit(surface, (int(self.pastPositions[x].x) - 5, int(self.pastPositions[x].y) - 5))
            #pygame.draw.circle(screen, (255, 255, 255), (int(self.pastPositions[x].x), int(self.pastPositions[x].y)), int(self.size), 0)
        
attractor = Body(screenSize / 2.0, Vector(0.0, 0.0), 200.0)
sattelite = Body(screenSize / 4.0, Vector(67.5, -67.5), 20.0)

bodies = []

bodies.append(sattelite)
bodies.append(attractor)

newBody = Body(screenSize / 4.2, Vector(8.0, -8.0), 1.0)
bodies.append(newBody)

#newBody = Body(screenSize / 5.0, Vector(5.0, -5.0), 1.0)
#bodies.append(newBody)

#newBody = Body(Vector(screenSize.x, 0.0), Vector(-200.0, 400.0), 100.0)
#bodies.append(newBody)

while True:
    pygame.event.pump()
    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[K_ESCAPE]:
        pygame.quit()
        break
    
    if pressedKeys[K_UP]:
        TIME_FACTOR += 0.03
    elif pressedKeys[K_DOWN]:
        TIME_FACTOR -= 0.03

    if TIME_FACTOR > 0.5:
        TIME_FACTOR = 0.5
    elif TIME_FACTOR < 0.0:
        TIME_FACTOR = 0.0
    
    for body in bodies:
        for otherBody in bodies:
            if body is not otherBody:
                body.calculateAttraction(otherBody)

    for body in bodies:
        body.updatePosition()

    screen.fill((0, 0, 0))

    for body in bodies:
        body.draw()
    
    pygame.display.flip()
