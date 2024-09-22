# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:50:13 2024

@author: akmal
"""

import pygame
import math
import imageio
from PIL import Image
import os

pygame.init()

WIDTH, HEIGHT = 800, 800

# Setup Pygame Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting a title to the window
pygame.display.set_caption("Planet Simulation")

# RGB value color
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (138, 39, 50)
DARK_GREY = (80, 78, 81)

# Making planets for the system
class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98812 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    # Directory to save frames
    save_path = "D:/self_project/frames"  # Make sure this folder exists
    os.makedirs(save_path, exist_ok=True)  # Create the directory if it doesn't exist

    # List to store frames
    frames = []
    frame_count = 0  # Keep track of the frame number
    
    while run:
        clock.tick(60)  # Number of frames per second
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        # Save the current frame
        pygame.display.update()
        frame_filename = os.path.join(save_path, f"frame_{frame_count}.png")
        pygame.image.save(WIN, frame_filename)
        img = Image.open(frame_filename)
        frames.append(img)
        frame_count += 1

    pygame.quit()

    # Save frames as a GIF
    gif_path = os.path.join(save_path, 'simulation.gif')
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"GIF saved at: {gif_path}")


main()

