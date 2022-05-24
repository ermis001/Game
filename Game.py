import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Knight Rush")
icon = pygame.image.load('icon.knight.png')
pygame.display.set_icon(icon)

jump = False
velx = 10
vely = 20

#Knight creation

knight_img = pygame.image.load('pixel.knight.png')
rect = knight_img.get_rect()

rect.x = 200
rect.y = 450

#Obstacle


enmy_speed = 5
enemysiz = (50, 80)
obstacle_pos = [900, 550]
obstacle = pygame.Rect(obstacle_pos[0], obstacle_pos[1], 50, 90)       
        
#Score
score = 0
myFont = pygame.font.SysFont("monospace", 30)    
        

def knight():
        screen.blit(knight_img, (rect))  #Printing knight in screen


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    userinput = pygame.key.get_pressed()
    if userinput[pygame.K_a] and rect.x>0:
        rect.x -= 10
    if userinput[pygame.K_d] and rect.x<780:
        rect.x += 10    

    if jump is False and userinput[pygame.K_w]:
        jump = True
        
    if jump is True:
            rect.y -= vely
            vely -= 1
            if vely < -20:
                jump= False
                vely = 20  

    pygame.draw.rect(screen ,(200,0,0), obstacle)

    if obstacle.x >= 0 and obstacle.x <= 900:
        obstacle.x -= enmy_speed
    else:
        obstacle.y = random.randint(obstacle_pos[1]-40, obstacle_pos[1])
        obstacle.x = 900
        score += 10

#Print score
    text = "Score:" + str(score)
    label = myFont.render(text, 1, (255,255,255))
    screen.blit(label, (50, 30))    

#Speed system
    if score <= 100:
        enmy_speed = 5
    elif score > 100:
        enmy_speed = 9
    elif score > 200:
        enmy_speed = 13
    elif score > 300:
        enmy_speed = 17
    elif score > 400:
        enmy_speed = 21
    elif score > 500:
        enmy_speed = 25
    else: enmy_speed = 30    

    if rect.colliderect(obstacle):
        break
        
            

    knight()

    pygame.display.update()        
    pygame.time.delay(15)