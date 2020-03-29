import pygame
import math
import os
from constants import *

os.environ['SDL_VIDEO_CENTERED']='1'


pygame.init()
pygame.display.set_caption("Julia Set")

screen = pygame.display.set_mode((Width, Height))

fractal_list = pygame.PixelArray(screen)
incr = borders*((max_x - offset_x)/(float(Width)))



def complex_y(a):
    return int(((Height)/(offset_y - max_y)*a) + (Height * max_y)/(max_y - offset_y))

def complex_x(a):
    return int(((Width)/(max_x - offset_x)*a) + (Width * offset_x)/(offset_x - max_x))

def frange(start, end, increment):
    current = start
    outputList = [float('%10.75f' % current)]
    while current < end:
        current += increment
        outputList = outputList + [float('%10.75f' % current)]
    return outputList

list1 = frange(offset_x,max_x,incr)
list2 = frange(offset_y,max_y,incr)

for x in list1:
    for y in list2:
        z = complex(x,y)
        point = z
        accuracy = 0
        while accuracy < iterations and abs(z) < 2.0:
            z = z*z + complex_number
            accuracy += 1

        if accuracy == iterations:
            x1 = complex_x(point.real)
            y1 = complex_y(point.imag)

            if x1 < Width and y1 < Height:
                if color_mode == 1:
                    fractal_list[x1,y1] = (12, 211, 192)

                if color_mode == 2:
                    fractal_list[x1,y1] = (0,0,0)
        if accuracy < iterations:

            x1 = complex_x(point.real)
            y1 = complex_y(point.imag)
            if color_mode == 1:
                _n = 75* math.log10(accuracy )

                if x1 < Width and y1 < Height and y1 > 0 and x1 > 0:
                    fractal_list[x1,y1] = (24,_n,_n)

    pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
