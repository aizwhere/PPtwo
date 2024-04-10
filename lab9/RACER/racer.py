import pygame
import sys
import random

pygame.init()

score1 = 0
CL = 60
weight = 400
height = 600
step = 5
e_step = 8
coin_step = 8
clock = pygame.time.Clock()
screen = pygame.display.set_mode((weight, height))
bg = pygame.image.load("RACER/AnimatedStreet.png")
font = pygame.font.SysFont("comicsansms", 20)


# settings for red car
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RACER/Player.png ")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.move_ip(0, e_step)
        if self.rect.top > height:
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # setting for coin


class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RACER/coin.png")
        self.small = pygame.transform.scale(self.image, (20, 20))
        self.big = pygame.transform.scale(self.image, (50, 50))
        self.ls = [self.small, self.big]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        self.rect.move_ip(0, coin_step)
        if self.rect.bottom > height:
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self):
        screen.blit(self.rand, self.rect.topleft)

    def collide(self):
        self.rand = random.choice(tuple(self.ls))
        self.rect.center = (random.randint(30, 350), 0)

    # setting for blue car


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RACER/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (150, 520)

    def update(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-step, 0)
        if self.rect.right < weight:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(step, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    # spirit groups


p1 = player()
e1 = enemy()
c1 = coin()
all_sprite = pygame.sprite.Group()
all_sprite.add(e1)
all_sprite.add(c1)
all_sprite.add(p1)
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(e1)
coins.add(c1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    score = font.render(str(c1.counter), True, (0, 128, 0))
    p1.update()
    e1.update()
    c1.update()
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(p1, coins):
        c1.collide()
        if c1.rand == c1.big:
            c1.counter += 2
            e_step += 1
        if c1.rand == c1.small:
            c1.counter += 1
            e_step += 0.5

    if pygame.sprite.spritecollideany(c1, enemies):
        c1.collide()

    screen.blit(bg, (0, 0))
    screen.blit(score, (weight - score.get_width() - 10, 0))

    p1.draw(screen)
    e1.draw(screen)
    c1.draw()

    pygame.display.update()
    clock.tick(CL)