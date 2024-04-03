import pygame
import random

pygame.init()

width, height = 600, 600 
coin_img = pygame.image.load("COIN/coin.png")

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("collecting coins")
pygame.display.set_icon(coin_img)
coin_img = pygame.transform.scale(coin_img, (40, 40)) 

player_x = width // 2
player_y = height - 100

coins = []
collected_coins = 0

clock = pygame.time.Clock()

player_speed = 10

collectext = pygame.font.Font("text.ttf", 15)

running  = True
while running:
    screen.fill((255, 153, 153))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if random.randint(0, 100) < 3:
        coin = coin_img.get_rect(center=(random.randint(20, width-20), 0))      
        coins.append(coin)  

    for coin in coins:
        coin.y += 3
        player = pygame.Rect(player_x, player_y, 40, 40)

        if coin.colliderect(player):
            collected_coins += 1
            coins.remove(coin)
        if coin.y > height - 40:
            coins.remove(coin)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        player_x = min(width - 40, player_x + player_speed)       
    if pressed[pygame.K_LEFT]:
        player_x = max(0, player_x - player_speed)

    screen.fill    

    text = collectext.render("COINS:" + str(collected_coins), True, "purple")   
    screen.blit(text, (width - 150, 30))

    pygame.draw.rect(screen, "purple", (player_x, player_y, 40, 40))

    for coin in coins:
        screen.blit(coin_img, coin)



    pygame.display.update()
    clock.tick(60)
pygame.quit()    