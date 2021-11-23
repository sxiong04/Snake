import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self):
        pass

    def draw(self):
        pass


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


                elif keys[pygame.K_RIGHT]:

                elif keys[pygame.K_DOWN]:

                elif keys[pygame.K_UP]:

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self):
        pass


def draw_grid(w, rows, surface):
    size_between = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)

    pass


main()
