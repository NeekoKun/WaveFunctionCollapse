import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from wfc import WFC
import pygame

SIZE = WIDTH, HEIGHT = 700, 700
sprites_width, sprites_height = 100, 100
pygame.display.init()
screen = pygame.display.set_mode(SIZE)

wfc = WFC(7, 7)
random.seed(0)

wfc.set_mode("adjacency")

wfc.assign_rules("mountain", ["mountain", "forest"])
wfc.assign_rules("forest", ["mountain", "forest", "beach"])
wfc.assign_rules("beach", ["forest", "beach", "sea"])
wfc.assign_rules("sea", ["beach", "sea"])

grid = wfc.generate_grid()

sprites = {}
sprites["mountain"] = pygame.image.load("sprites/mountain.png")
sprites["forest"] = pygame.image.load("sprites/forest.png")
sprites["beach"] = pygame.image.load("sprites/beach.png")
sprites["sea"] = pygame.image.load("sprites/sea.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((255, 255, 255))
    
    for y, row in enumerate(grid):
        for x, i in enumerate(row):
            screen.blit(sprites[i], (x*sprites_width, y*sprites_height))
    
    pygame.display.flip()