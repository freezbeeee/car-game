import pygame
import math

#Initialisation
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Création de la voiture du joueur :
car = pygame.image.load("Voitures/1.png").convert_alpha()
car = pygame.transform.scale(car, (100, 50))
car_rect = car.get_rect()
car_rect.x = 1280 / 2 - 50
car_rect.y = 1080 / 2 - 25
theta = 0
speed = 5

#Définition du mouvement (basique) de la voiture
def car_movement():
    global car
    global car_rect
    global theta
    global speed
    
    if theta == -180:
        theta = 180
    elif theta == 270:
        theta = -90
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car = pygame.transform.rotate(car, 15)
        car_rect = car.get_rect(center=car_rect.center)
        theta += 15
    if keys[pygame.K_RIGHT]:
        car = pygame.transform.rotate(car, -15)
        car_rect = car.get_rect(center=car_rect.center)
        theta -= 15
    if keys[pygame.K_UP]:
        car_rect.x += speed * math.cos(math.radians(theta))
        car_rect.y -= speed * math.sin(math.radians(theta))
    if keys[pygame.K_DOWN]:
        car_rect.x -= speed * math.cos(math.radians(theta))
        car_rect.y += speed * math.sin(math.radians(theta))   
    screen.blit(car, (car_rect.x, car_rect.y))


#Execution du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0)) 
        car_movement()
        pygame.display.flip()
        clock.tick(30)
    

pygame.quit()
