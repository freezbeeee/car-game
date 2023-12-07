import pygame
from constants import *
from car import car

#Initialisation
pygame.init()
clock = pygame.time.Clock()
running = True
dt = clock.get_time() / 1000

#Execution du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        car.controls(car, pygame.key.get_pressed())
        car.calculate(car, dt)
        car.update(car)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
