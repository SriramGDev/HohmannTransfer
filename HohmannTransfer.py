import pygame
from pygame.locals import *
from sys import exit
import time
import multiprocessing

import math

pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h ), pygame.FULLSCREEN)
font = pygame.font.SysFont("monospace", 11)

def degreesToRadians(deg):
    return deg/180.0 * math.pi

def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)

    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (127, 127, 0)
black = (0, 0, 0)

angle_e = angle_m = degreesToRadians(-35)
angle_s = degreesToRadians(60)
x_s = 750
y_s = 450
points = []
day = 0
isFirst = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill(black)
    drawCircleArc(screen, yellow, (0, pygame.display.Info().current_h/2), 400, -90, 180, 400)
    drawCircleArc(screen, white, (0, pygame.display.Info().current_h/2), 750, -90, 180, 2)
    drawCircleArc(screen, white, (0, pygame.display.Info().current_h/2), 1250, -90, 180, 2)
    cor_x = 0
    cor_y = pygame.display.Info().current_h/2
    cor_x_s = 1000
    cor_y_s = 90
    radius_s = 450
    omega_s = 0.00185
    radius_e = 750
    radius_m = 1250
    omega_e = 0.001
    omega_m = 0.0005

    x_e = cor_x + radius_e * math.cos(angle_e)
    y_e = cor_y - radius_e * math.sin(angle_e)
    x_m = cor_x + radius_m * math.cos(angle_m)
    y_m = cor_y - radius_m * math.sin(angle_m)
    earth = screen.blit(pygame.image.load("earth.png"), (x_e-25, y_e-25))
    mars = screen.blit(pygame.image.load("mars.png"), (x_m-25, y_m-25))
    angle_e = angle_e + omega_e
    angle_m = angle_m + omega_m
    if angle_e > 0:
        prev_x_s = x_s
        prev_y_s = y_s
        x_s = cor_x_s - radius_s * math.cos(angle_s)
        y_s = cor_y_s + radius_s * math.sin(angle_s)
        points.append((prev_x_s, prev_y_s))
        points.append((x_s, y_s))
        pygame.draw.lines(screen, green, False, points)
        spacecraft = screen.blit(pygame.transform.rotate(pygame.image.load("orbiter_small.png"), angle_s), (x_s-40, y_s-25))
        angle_s = angle_s + omega_s
    pygame.display.flip()

    if angle_m > 0:
        end = time.time()
        time.sleep(2)
        angle_m = angle_e = degreesToRadians(-35)
        angle_s = degreesToRadians(60)
        points = []
        x_s = 750
        y_s = 450
    pygame.display.update()
