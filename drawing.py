#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Drawing game elements """
import pygame
from settings import *
from map import mini_map
from collections import deque
from random import randrange
import sys


class Drawing:
    def __init__(self, sc, sc_map, player, clock):
        self.shot_projection = 0
        self.sc = sc
        self.sc_map = sc_map
        self.player = player
        self.clock = clock
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.font_win = pygame.font.Font("font/font.ttf", 144)
        self.textures = {
            1: pygame.image.load("img/wall3.png").convert(),
            2: pygame.image.load("img/wall4.png").convert(),
            3: pygame.image.load("img/wall5.png").convert(),
            4: pygame.image.load("img/wall6.png").convert(),
            "sky": pygame.image.load("img/sky2.png").convert()
        }
        # menu
        self.menu_trigger = True
        self.menu_picture = pygame.image.load("img/bg.jpg").convert()
        # weapon parameters
        self.weapon_base_sprite = pygame.image.load("sprites/weapons/shotgun/base/0.png").convert_alpha()
        self.weapon_shot_animation = deque([pygame.image.load(f'sprites/weapons/shotgun/shot/{i}.png').convert_alpha()
                                            for i in range(20)])
        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 2, HEIGHT - self.weapon_rect.height)
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_speed = 3
        self.shot_animation_count = 0
        self.shot_animation_trigger = True
        self.shot_sound = pygame.mixer.Sound("sound/shotgun.wav")
        # sfx parameters
        self.sfx = deque([pygame.image.load(f"sprites/weapons/sfx/{i}.png").convert_alpha() for i in range(9)])
        self.sfx_length_count = 0
        self.sfx_length = len(self.sfx)

    def background(self, angle):
        """
        Drawing sky and floor
        :param angle: angle value
        :return:
        """
        # drawing sky
        # calculating offset by texture (reversed_player_direction MOD screen_width)
        sky_offset = -10 * math.degrees(angle) % WIDTH
        # drawing 3 sky pieces, depending on the player's shift (to make texture seams not notable)
        self.sc.blit(self.textures["sky"], (sky_offset, 0))
        self.sc.blit(self.textures["sky"], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures["sky"], (sky_offset + WIDTH, 0))
        # drawing floor
        pygame.draw.rect(self.sc, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        """ drawing walls and sprites (sprites structure is the same with walls). Uses Z-buffer algorithm. """
        # sort them by depth and begin their drawing with the furthest objects (Z-buffer algorithm)
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            # ignore false values for sprites
            if obj[0]:
                # unpack tuple
                _, object, object_pos = obj
                # put objects on the main surface
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        """ FPS output """
        display_fps = "FPS: %s" % int(clock.get_fps())
        render = self.font.render(display_fps, 0, DARKORANGE)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        # set direction by drawing the line, which length equals the screen length
        # player's view point coordinates calculations using sin and cos
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)

        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

    def player_weapon(self, shots):
        if self.player.shot:
            if not self.shot_length_count:
                self.shot_sound.play()
            # define what's closer: wall or sprite (using min distance)
            self.shot_projection = min(shots)[1] // 2

            self.bullet_sfx()

            shot_sprite = self.weapon_shot_animation[0]
            self.sc.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            if self.shot_animation_count == self.shot_animation_speed:
                self.weapon_shot_animation.rotate(-1)
                self.shot_animation_count = 1
                self.shot_length_count += 1
                self.shot_animation_trigger = False
            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.sfx_length_count = 0
                self.shot_animation_trigger = True
        else:
            self.sc.blit(self.weapon_base_sprite, self.weapon_pos)

    def bullet_sfx(self):
        """
        Bullet explosion effect
        :return:
        """
        if self.sfx_length_count < self.sfx_length:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_projection, self.shot_projection))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx, (HALF_WIDTH - sfx_rect.w // 2, HALF_HEIGHT - sfx_rect.h // 2))
            self.sfx_length_count += 1
            self.sfx.rotate(-1)

    def win(self):
        """ Output victory message at the end of the game"""
        # output centered rounded black rectangle
        # change congratulation in the red color range
        render = self.font_win.render("YOU WIN!!!", 1, (randrange(40, 120), 0, 0))
        rect = pygame.Rect(0, 0, 1000, 300)
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, BLACK, rect, border_radius=50)
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 140))
        pygame.display.flip()
        self.clock.tick(15)

        # Escape button = exit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

    def menu(self):
        x = 0
        button_font = pygame.font.Font('font/font.ttf', 72)
        label_font = pygame.font.Font('font/font1.otf', 400)
        start = button_font.render('START', 1, pygame.Color('lightgray'))
        button_start = pygame.Rect(0, 0, 400, 150)
        button_start.center = HALF_WIDTH, HALF_HEIGHT
        exit = button_font.render('EXIT', 1, pygame.Color('lightgray'))
        button_exit = pygame.Rect(0, 0, 400, 150)
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200

        pygame.mixer.music.load('sound/menu.mp3')
        pygame.mixer.music.play()

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # background picture moves slowly by X coordinate
            self.sc.blit(self.menu_picture, (0, 0), (x % WIDTH, HALF_HEIGHT, WIDTH, HEIGHT))
            x += 1

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            # game name color randomly changes in the grey color range
            color = randrange(40)
            label = label_font.render('DOOOOM', 1, (color, color, color))
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    pygame.mixer.music.stop()
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

            # set fps
            self.clock.tick(20)
