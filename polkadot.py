#Pygame
import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

#Window
window_height = 800
window_width = 1000

window = pygame.display.set_mode(size = (window_width,window_height))
pygame.display.set_caption('MyGame')

#Big fish lists
#bigfish_positions = []
#bigfish_velocities = []
big_fishes = []
big_fishes_rects = []

RED = (255,0,0)

#Constants
max_dots = 20
score = 0
bg_colour = "white"
big_fish_upper_lim = 100
big_fish_lower_lim = 2

# Possible starting positions
l1 = [window_width,0]
l2 = [0, window_height]

#l1 = [window_width + 30, -30]
#l2 = [-30, window_height + 30]


class Fish(pygame.sprite.Sprite):
    def __init__(self, colour, radius, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x,self.y)
        self.radius = radius
        self.colour = colour
        self.vx = 0
        self.vy = 0


    def update(self):
        pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)
        self.rect = pygame.Rect(window_width - (self.x + self.radius), window_height - (self.y + self.radius), self.radius, self.radius)


def choose_velocity(fish):
    if fish.x <= 0:
        fish.vx = random.uniform(0.1,5)
    else:
        fish.vx = random.uniform(-5,-0.1)
    if fish.y <= 0:
        fish.vy = random.uniform(0.1,5)
    else:
        fish.vy = random.uniform(-5,-0.1)


def generateFish():
    #Generating fish starting positions
    rw = random.randint(0,window_width)
    rh = random.randint(0, window_height)

    #rw = random.randint(-30, window_width + 30)
    #rh = random.randint(-30, window_height + 30)

    a1 = random.choice(l1)
    a2 = random.choice(l2)
    x = [a1,rw]
    x = random.choice(x)

    if x == a1:
        y = rh
    else:
        y = a2

    #bigfish_positions.append((x,y))


    colores = (random.randint(0,200),random.randint(0,200),random.randint(0,200))
    radius = random.randint(big_fish_lower_lim,big_fish_upper_lim)
    Fish1 = Fish(colores,radius,x,y)

    # Generating fish velocities
    choose_velocity(Fish1)
    choose_velocity(Fish1)

    return Fish1

# Starting fish should probably get rid of this since the fish will automatically spawn in the first frame
for i in range(10):
    f1 = generateFish()
    big_fishes.append(f1)

player = Fish("red",10,window_width/2,window_height/2)


def player_movement():
    pygame.mouse.set_visible(False)
    player.x = pygame.mouse.get_pos()[0]
    player.y = pygame.mouse.get_pos()[1]


def fish_movement(fish):
    fish.x += fish.vx
    fish.y += fish.vy


def fish_spawn(fish):
    if fish.x <= -50 or fish.x >= window_width + 50:
        try:
            big_fishes.remove(fish)
        except:
            pass
    if fish.y <= -50 or fish.y >= window_height + 50:
        try:
            big_fishes.remove(fish)
        except:
            pass
    if len(big_fishes) < 20:
        f1 = generateFish()
        big_fishes.append(f1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(bg_colour)

    #Ensures that there is the right amount of fish in the pond
    for bigfish in big_fishes:
        fish_movement(bigfish)
        bigfish.update()
        fish_spawn(bigfish)

    print(clock.get_fps())
    player.update()
    player_movement()

    pygame.display.flip()
    clock.tick(60)
