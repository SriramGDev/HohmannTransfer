# Synopsis
A simulation of the Hohmann Transfer between Earth and Mars at the optimal point using the PyGame Library. Almost all of the code was written in one sleepless night for the purpose of presenting an extremely basic working visualization of the Hohmann Transfer (in this case, to get to Mars).

# Code Example
```python
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
```
(Yeah, I know it isn't clean code and there are no comments. Maybe I'll make it more readable in the future)

# Motivation
This program was written for the Idaho Science and Aerospace Scholars Week 1 Camp thing. We wanted a simulation of the Hohmann Transfer so that the people we presented to could understand what "Getting There" actually entailed.

# Installation
The program relies on the Pygame library. That's available [here](http://www.pygame.org/download.shtml). The main program file is written in [Python 2.7](https://www.python.org/downloads/).

# Contributing
First off, I know that I should probably put this in another file, but I'm feeling lazy, so deal with it. If you want to contribute to the code, please feel free to submit a pull request. If you find any bugs, report them. If the program crashes because you didn't follow the Installation instructions properly, go follow the Installation instructions properly.

# TODO
1. Make everything more readable
  * Add comments
  * Change variable names
  * Partition code into functions
2. Add some statistics (multithreading?)
  * Fuel burned
  * Altitude above Earth
  * Time
  * Distance to Mars

# License
There is none. Do whatever you want with this code (so long as it's legal I guess). I really don't care.
