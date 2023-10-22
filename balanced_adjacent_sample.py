import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from wfc import WFC
import pygame

SIZE = WIDTH, HEIGHT = 700, 700
sprites_width, sprites_height = 100, 100
pygame.display.init()
screen = pygame.display.set_mode(SIZE)

wfc = WFC(100, 100)

mountain_color = (31, 45, 45)
forest_color = (0, 102, 0)
beach_color = (255, 204, 0)
sea_color = (0, 102, 255)

wfc.set_mode("balanced_adjacency")

wfc.assign_rules("mountain", ["mountain", "forest"])
wfc.assign_rules("forest", ["mountain", "forest", "beach"])
wfc.assign_rules("beach", ["forest", "beach", "sea"])
wfc.assign_rules("sea", ["beach", "sea"])


grid = wfc.generate_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((255, 255, 255))
    
    for y, row in enumerate(grid):
        for x, i in enumerate(row):
            match i:
                case "mountain":
                    pygame.draw.rect(screen, mountain_color, (y*7, x*7, 7, 7))
                case "forest":
                    pygame.draw.rect(screen, forest_color, (y*7, x*7, 7, 7))
                    pass
                case "beach":
                    pygame.draw.rect(screen, beach_color, (y*7, x*7, 7, 7))
                    pass
                case "sea":
                    pygame.draw.rect(screen, sea_color, (y*7, x*7, 7, 7))
                    pass
                case _:
                    pass
    
    pygame.display.flip()