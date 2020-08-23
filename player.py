#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Player's control """
from settings import *
import pygame
import math
from map import collision_walls


class Player:
    def __init__(self, sprites):
        self.x, self.y = player_pos
        self.sprites = sprites
        self.angle = player_angle
        self.sensitivity = 0.004    # mouse sensitivity
        # collision parameters
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        # weapon
        self.shot = False

    @property
    def pos(self):
        return self.x, self.y

    @property
    def collision_list(self):
        """ All collision. Sprites with collsions taking into account the following params: size, position, blocked. """
        return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
                                  self.sprites.list_of_objects if obj.blocked]

    def detect_collision(self, dx, dy):
        # copy current pos
        next_rect = self.rect.copy()
        # move to dx, dy
        next_rect.move_ip(dx, dy)
        # create collision walls indexes
        hit_indexes = next_rect.collidelistall(self.collision_list)

        # find collision side. There can be several collisions.
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.top
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def keys_control(self):
        """ Detect pressed controls and change player's direction """
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        # using trigonometric reduction formulas
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.shot:
                    self.shot = True

    def mouse_control(self):
        # when mouse pointer is in the game screen
        if pygame.mouse.get_focused():
            # calculate current X coord - screen center
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            # on every iteration: move mouse pointer to the screen center
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            # add this difference tot the player's direction angle (regarding mouse sensitivity)
            self.angle += difference * self.sensitivity
