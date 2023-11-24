import pygame
import math

#Initialisation
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
pygame.key.set_repeat(50,0)

#Création de la voiture du joueur :
car = pygame.image.load("Voitures/1.png").convert_alpha()
car_rect = car.get_rect()
car_rect.x = 500 / 2 - 50
car_rect.y = 500 / 2 - 25
theta = 0
speed = 5

#Définition du mouvement de la voiture 
def car_movement():
    global car
    global car_rect
    global theta

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if keys[pygame.K_LEFT]:
            theta -= 5
        if keys[pygame.K_RIGHT]:
            theta += 5
        car_rect.x += speed * math.cos(math.radians(theta))
        car_rect.y += speed * math.sin(math.radians(theta))
    if keys[pygame.K_DOWN]:
        if keys[pygame.K_LEFT]:
            theta -= 5
        if keys[pygame.K_RIGHT]:
            theta += 5
        car_rect.x -= speed * math.cos(math.radians(theta))
        car_rect.y -= speed * math.sin(math.radians(theta))

    car_no_rotation = pygame.transform.rotate(car, -theta)
    car_rect = car_no_rotation.get_rect(center=car_rect.center)
    screen.blit(car_no_rotation, (car_rect.x, car_rect.y))
    #print('theta : ', theta, 'car_rect.x : ', car_rect.x, 'car_rect.y : ', car_rect.y)

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
