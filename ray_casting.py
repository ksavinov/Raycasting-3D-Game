#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Ray casting mechanism, accelerated with numba library """
import pygame
from settings import *
from map import world_map
from map import WORLD_WIDTH
from map import WORLD_HEIGHT
from numba import njit


@njit(fastmath=True)
def mapping(a, b):
    """ Coordinates of the upper left corner (square) in which we are at the moment """
    return (a // TILE) * TILE, (b // TILE) * TILE


@njit(fastmath=True)
def ray_casting(player_pos, player_angle, world_map):
    casted_walls = []
    # ray coordinates
    ox, oy = player_pos
    texture_v, texture_h = 1, 1  # fix ZeroDivisionError, when player goes beyond the map
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    # iterate through all the rays
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # Bresenham's line algorithm
        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        # iterate through screen width (step = TILE)
        for i in range(0, WORLD_WIDTH, TILE):
            # find vertical distance
            depth_v = (x - ox) / cos_a
            # its Y coordinate
            yv = oy + depth_v * sin_a
            # check collision with wall
            # if there was no intersection, go to the next vertical
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                # defines number of required texture
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # horizontals (calculating similarly as verticals)
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                # defines number of required texture
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection (which point of intersection (with a vertical or horizontal line) is closer to the player)
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        # calculate the offset by finding the remainder of the division from the TILE
        offset = int(offset) % TILE
        # fixes the "fish-eye" effect that occurs when using Euclidean distances
        depth *= math.cos(player_angle - cur_angle)
        # calculate the projected height of the wall
        depth = max(depth, 0.00001)
        proj_height = (int(PROJ_COEFF / depth))

        # to list: distance to wall, texture offset, wall projection height, texture number
        # will be used to implement Z-buffer, when drawing begins from furthest objects
        casted_walls.append((depth, offset, proj_height, texture))

        # If instead of texture painting the walls in one color:
        # # add color depth (calculation based on distance)
        # c = 255 / (1 + depth * depth * 0.00002)
        # # pink :)
        # color = (c, c // 4, c)
        # # on each ray display the projection height of the wall as a rectangle
        # # отобразить проекционную высоту стены в виде прямоугольника на каждом луче
        # pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

        cur_angle += DELTA_ANGLE  # change angle for another ray
    return casted_walls


def ray_casting_walls(player, textures):
    """
    Texture shaping calculations only
    :param player:
    :param texture:
    :return:
    """
    casted_walls = ray_casting(player.pos, player.angle, world_map)
    wall_shot = casted_walls[CENTER_RAY][0], casted_walls[CENTER_RAY][2]
    walls = []
    for ray, casted_values in enumerate(casted_walls):
        depth, offset, proj_height, texture = casted_values
        # solving the problem of FPS drawdown when player come closely to the walls
        if proj_height > HEIGHT:
            coeff = proj_height / HEIGHT
            texture_height = TEXTURE_HEIGHT / coeff
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE,
                                                       HALF_TEXTURE_HEIGHT - texture_height // 2,
                                                       TEXTURE_SCALE,
                                                       texture_height)
            wall_column = pygame.transform.scale(wall_column, (SCALE, HEIGHT))
            wall_pos = (ray * SCALE, 0)
        else:
            # select a subsurface from the texture as a square,
            # where the initial coordinates equals the calculated texture offset
            # and width/height is imported from settings
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            # scale the selected texture piece to rectangle
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            # calculating position for texture
            wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
        walls.append((depth, wall_column, wall_pos))
    return walls, wall_shot
