import pygame
import sys
import os
size=width,height=1920,1080
resources=os.getcwd()+'/resources/'
def intialize ():
    pygame.init()
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("onimai monogatari")
    icon=pygame.image.load(resources+'icon.jpg')
    pygame.display.set_icon(icon)

def main (intialize):
    intialize

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
main(intialize())
