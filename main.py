from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from wfc import WFC
import pygame

SIZE = WIDTH, HEIGHT = 700, 700
sprites_width, sprites_height = 100, 100
pygame.display.init()
screen = pygame.display.set_mode(SIZE)

wfc = WFC(7, 7)

wfc.assign_rules("blank", {"0 1": 0, "1 0": 0, "0 -1": 0, "-1 0": 0})
wfc.assign_rules("top",   {"0 1": 1, "1 0": 0, "0 -1": 1, "-1 0": 1})
wfc.assign_rules("right", {"0 1": 1, "1 0": 1, "0 -1": 0, "-1 0": 1})
wfc.assign_rules("bot",   {"0 1": 1, "1 0": 1, "0 -1": 1, "-1 0": 0})
wfc.assign_rules("left",  {"0 1": 0, "1 0": 1, "0 -1": 1, "-1 0": 1})

grid = wfc.generate_grid()

sprites = {}
sprites["blank"] = pygame.image.load("sprites/blank.png")
sprites["top"] = pygame.image.load("sprites/top.png")
sprites["bot"] = pygame.image.load("sprites/bot.png")
sprites["left"] = pygame.image.load("sprites/left.png")
sprites["right"] = pygame.image.load("sprites/right.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((255, 255, 255))
    
    for y, row in enumerate(grid):
        for x, i in enumerate(row):
            screen.blit(sprites[i], (x*sprites_width, y*sprites_height))
    
    pygame.display.flip()