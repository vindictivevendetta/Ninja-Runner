from tkinter import Menu
import pygame, sys, random, os

pygame.init()
screen= pygame.display.set_mode((1100,700))
clock = pygame.time.Clock()
pygame.display.set_caption("Ninja Runner")

TOMBSTONE1 = [pygame.image.load(os.path.join("assets/TombStone1.png")),
              pygame.image.load(os.path.join("assets/TombStone1.png"))]

TOMBSTONE2 = [pygame.image.load(os.path.join("assets/TombStone2.png")),
              pygame.image.load(os.path.join("assets/TombStone2.png"))]

DEAD_BUSH = [pygame.image.load(os.path.join("assets/DeadBush1.png")),
             pygame.image.load(os.path.join("assets/DeadBush2.png"))]

SKELETON = [pygame.image.load(os.path.join("assets/skeleton.png")),
            pygame.image.load(os.path.join("assets/skeleton.png"))]

BIRD = [pygame.image.load(os.path.join("assets/bat1.png")),
        pygame.image.load(os.path.join("assets/bat2.png"))]

start_img=pygame.image.load("assets/buttons.png")
quit_img=pygame.image.load("assets/Buttons2.png")

# BackGround Begins

black=(0,0,0)
c=1100
d=700
display_surface=pygame.display.set_mode((c,d))
image=pygame.image.load('assets/BG.png')

# Classes

class Ninja(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_1.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_2.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_3.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_4.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_5.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_6.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_7.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_8.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_9.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_10.png"), (80, 100)))

        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking1.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking2.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking3.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking4.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking5.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking6.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking7.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking8.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking9.png"),(110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/ninja_ducking10.png"),(110, 60)))

        self.x = x_pos
        self.y = y_pos

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.velocity = 50
        self.gravity = 4.5
        self.ducking = False
    
    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 1.1
        if self.current_image > 10:
            self.current_image = 0
        
        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]  
        else:
            self.image = self.running_sprites[int(self.current_image)]
        
    def duck(self):
        self.ducking = True
        self.rect.centery = 450
    
    def unduck(self):
        self.ducking = False
        self.rect.centery = 402

    def apply_gravity(self):
        if self.rect.centery <= 402:
            self.rect.centery += self.gravity
    
    def jump(self):
        if self.rect.centery >= 402:
            while self.rect.centery - self.velocity > 220:
                self.rect.centery -= 1
    
class Obstacle:
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1200

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class TombStone1(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 400

class Tombstone2(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 376

class DeadBush(Obstacle): 
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 390

class Skeleton (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)  
        self.rect.y = 405

class Bird (Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 350
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Button1():
    def __init__(self,x,y, image, scale):
        width=image.get_width()
        height=image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        [x,y]=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            print(pos)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True  
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        display_surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Variables
global game_speed, obstacles
game_speed = 14
obstacles = []
player = Ninja(80,100)
points = 0
font = pygame.font.Font('freesansbold.ttf', 20)
death_count = 0 
start_button = Button1(360,500,start_img,0.8)
quit_button = Button1(610,500,quit_img,0.8)

def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1
    text = font.render("POINTS: " + str(points), True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (1000,40)
    screen.blit(text, textRect)

# Surfaces

ground = pygame.image.load("assets/BG.png")
ground_rect = ground.get_rect(center=(640, 400))

floor = pygame.image.load("assets/floor_3.png")
floor = pygame.transform.scale(floor, (1280,150))
floor_rect = floor.get_rect(center=(129,550))
floor_x = 0

# Groups

ninja_group = pygame.sprite.GroupSingle()

# Objects

ninja = Ninja(150, 402)
ninja_group.add(ninja)

#COMMS

font = pygame.font.SysFont(None, 40)
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [600/2, 700/2])

#pause
def pause():
    a=1100
    b=700
    display_surface=pygame.display.set_mode((a,b))
    pygame.display.set_caption("pause menu")
    paused = True 
    while paused:
        for even in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        display_surface.fill("white")
        message_to_screen("Press C to continue or press Q to quit.", (0,0,0))
        pygame.display.update()
        clock.tick(5)
                
def menu(death_count):
    global points
    run = True
    while run:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.Font("Better luck next time" , True, (0,0,0))
        elif death_count > 0:
            text = font.render("Better luck next time", True, (0,0,0))
            score = font.render("your score: " + str(points), True, (0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (1100 // 2 , 700 // 2 + 50)
            screen.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (1100 // 2, 700 // 2)
        screen.blit(text, textRect)
        pygame.display.update()
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                run = False
            if Event.type == pygame.KEYDOWN:
                continue

while True: 
    display_surface.fill(black)
    display_surface.blit(image, (-450,0))
    if start_button.draw() == True:
      print("start")
      while True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            ninja.duck()
        else:
            if ninja.ducking:
                ninja.unduck()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    ninja.jump()
                elif event.key == pygame.K_p:
                    pause()

        screen.fill("white")

        floor_x -= 14

        screen.blit(ground, ground_rect)
        screen.blit(floor, (floor_x, 450))
        screen.blit(floor, (floor_x + 1280, 450))

        if len(obstacles) == 0:
            if random.randint(0,5) == 0:
                obstacles.append(TombStone1(TOMBSTONE1))
            elif random.randint(0,5) == 1:
                obstacles.append(Tombstone2(TOMBSTONE2))
            elif random.randint(0,5) == 2:
                obstacles.append(DeadBush(DEAD_BUSH))
            elif random.randint(0,5) == 3:
                obstacles.append(Skeleton(SKELETON))
            elif random.randint(0,5) == 4:
                obstacles.append(Bird(BIRD))
            
        
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if ninja.rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
            
        ninja_group.update()
        ninja_group.draw(screen)

        if floor_x <= -1280:
            floor_x = 0
        
        score()

        pygame.display.update()
        clock.tick(30)

    if quit_button.draw():
        print("Exit")
        exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
