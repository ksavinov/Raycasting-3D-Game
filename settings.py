#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
All settings here
"""
import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT  # optimization for the projection height
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 60
TILE = 100  # map tile size
FPS_POS = (WIDTH - 155, 5)

# minmap settings
MINIMAP_SCALE = 5  # reduces the size of the map using this scale
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE  # 1 -> 12x8, 2 -> 24x16, 3 -> 36x24
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)  # minimap position

# ray cating settings
FOV = math.pi / 3   # FOV = field of view
HALF_FOV = FOV / 2
NUM_RAYS = 300      # rays number
MAX_DEPTH = 800     # render distance
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # scale coefficient to save resources
PROJ_COEFF = 3 * DIST * TILE  # x3, to prevent stretching the wall
SCALE = WIDTH // NUM_RAYS

# sprite settings
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
# using in sprite_objects, to prevent sprite disappearance, when its half hides behind wall
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE  # scale coefficient

# player settings
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0  # player's view direction
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 233, 246)
DARKGREY = (40, 40, 40)
PURPLE = (120, 0, 120)
PINK = (255, 105, 180)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)
