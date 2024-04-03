import pygame 
import random 
import sys 
 
BLACK = (0, 0, 0) 
LINE_COLOR = (50, 50, 50) 
HEIGHT = 400 
WIDTH = 400 
 
BLOCK_SIZE = 20 
 
class Point: 
    def __init__(self, _x, _y): 
        self.x = _x 
        self.y = _y 
 
class Food: 
    def __init__(self): 
        self.location = Point(4, 10) 
 
    def draw(self): 
        point = self.location 
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE) 
        pygame.draw.rect(SCREEN, (0, 255, 0), rect) 
 
class Wall: 
    def __init__(self): 
        self.wall2 =[] 
        self.lvl = [1,2,3,4,5] 
        self.level = 1 
        self.speed = 5 
 
    def levels(self): 
        f = open("level{}.txt".format(self.level), "r") 
        for y in range(0,(HEIGHT//BLOCK_SIZE)+1): 
            for x in range(0,(WIDTH//BLOCK_SIZE)+1): 
                if f.read(1) == "#": 
                    self.wall2.append(Point(x,y)) 
 
    #     print(self.level) 
    def update(self, snake) : 
         
        if  snake.num %4 == 0 and snake.num >= 4: 
            self.wall2.clear() 
            f = open("level{}.txt".format(self.level), "r") 
            #SCREEN.fill(BLACK) 
         
 
            self.level = self.lvl[self.level+1]-1 
            self.speed+=1 
            self.wall2.clear() 
            for y in range(0,(HEIGHT//BLOCK_SIZE)+1): 
                for x in range(0,(WIDTH//BLOCK_SIZE)+1): 
                    if f.read(1) == "#": 
                        self.wall2.append(Point(x,y)) 
     
 
 
 
    def draw(self): 
        for point in self.wall2: 
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE) 
            pygame.draw.rect(SCREEN, (226,135,67), rect) 
     
 
 
class Snake: 
    def __init__(self): 
        self.body = [Point(10, 12)] 
        #self.level = 1 
        self.dx = 0 
        self.dy = 0 
        self.num = 0 
        self.kx = 0 
        self.ky = 0 
 
    def move(self):     
        for i in range(len(self.body) - 1, 0, -1): 
            self.body[i].x = self.body[i-1].x 
            self.body[i].y = self.body[i-1].y 
 
        self.body[0].x += self.dx  
        self.body[0].y += self.dy  
     
        if self.body[0].x * BLOCK_SIZE > WIDTH: 
            self.body[0].x = 0 
         
        if self.body[0].y * BLOCK_SIZE > HEIGHT: 
            self.body[0].y = 0 
     
        if self.body[0].x < 0: 
            self.body[0].x = WIDTH / BLOCK_SIZE 
         
        if self.body[0].y < 0: 
            self.body[0].y = HEIGHT / BLOCK_SIZE 
     
    def draw(self): 
        point = self.body[0] 
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE) 
        pygame.draw.rect(SCREEN, (255, 0, 0), rect) 
 
 
        for point in self.body[1:]: 
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE) 
            pygame.draw.rect(SCREEN, (0, 255, 0), rect) 
 
    def check_collision(self, food,wall): 
        if self.body[0].x == food.location.x: 
            if self.body[0].y == food.location.y: 
                self.body.append(Point(food.location.x, food.location.y)) 
                self.kx = random.randint(1,19) 
                self.ky = random.randint(1,19) 
                food.location = Point(self.kx,self.ky) 
                self.num+=1 
                wall.update(self) 
         
         
 
        for i in wall.wall2: 
            if self.body[0].x == i.x: 
                if self.body[0].y == i.y: 
                    pygame.quit() 
                    sys.exit() 
        for i in wall.wall2: 
            if i.x == self.kx: 
                if i.y == self.ky: 
                    self.kx = random.randint(1,19) 
                    self.ky = random.randint(1,19) 
                    food.location = Point(self.kx,self.ky) 
         
def main(): 
    global SCREEN, CLOCK 
    pygame.init() 
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) 
    CLOCK = pygame.time.Clock() 
    SCREEN.fill(BLACK) 
    font = pygame.font.SysFont("comicsansms", 20) 
    food_font = pygame.font.SysFont("comicsansms", 20) 
    snake = Snake() 
    food = Food() 
    wall = Wall() 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT: 
                    snake.dx = 1 
                    snake.dy = 0 
                if event.key == pygame.K_LEFT: 
                    snake.dx = -1 
                    snake.dy = 0 
                if event.key == pygame.K_UP: 
                    snake.dx = 0 
                    snake.dy = -1 
                if event.key == pygame.K_DOWN: 
                    snake.dx = 0 
                    snake.dy = 1 
                 
        score = font.render("score food "+str(snake.num), True, (0, 128, 0)) 
        score_f = food_font.render("score level "+str(wall.level),True,(0,128,0)) 
        snake.move() 
 
        snake.check_collision(food,wall) 
        wall.levels()     
 
        SCREEN.fill(BLACK) 
         
         
        snake.draw() 
        food.draw() 
        wall.draw() 
         
        drawGrid() 
        SCREEN.blit(score_f,(WIDTH-score_f.get_width()-20,0)) 
        SCREEN.blit(score,(WIDTH-score.get_width()-20,25)) 
        pygame.display.update() 
        CLOCK.tick(wall.speed) 
 
 
def drawGrid(): 
    for x in range(0, WIDTH, BLOCK_SIZE): 
        for y in range(0, HEIGHT, BLOCK_SIZE): 
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE) 
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1) 
 
 
main()