import pygame
import math
from constants import screen, ENGINE

class car:
    def __init__(self):
        self.car = pygame.image.load("Voitures/1.png").convert_alpha()
        self.car_rect = self.car.get_rect()
        self.theta = 0
        self.x = 500
        self.y = 500
        self.engine = ENGINE
    
    def controls(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.theta -= 10
        elif keys_pressed[pygame.K_RIGHT]:
            self.theta += 10
        if keys_pressed[pygame.K_UP]:
            self.engine += 2
        elif keys_pressed[pygame.K_DOWN]:
            self.engine -= 1
    
    def calculate(self, dt):
        radians_theta = math.radians(self.theta)
        self.car_rect.y -= self.engine * math.sin(radians_theta) * dt
        self.car_rect.x -= self.engine * math.cos(radians_theta) * dt
        self.car_no_rotation = pygame.transform.rotate(self.car, -self.theta)
        self.car_rect = self.car_no_rotation.get_rect(center=self.car_rect.center)
    
    def update(self):
        screen.blit(self.car_no_rotation, (self.car_rect.x, self.car_rect.y))
