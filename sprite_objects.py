#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Sprites """
import pygame
from settings import *
from collections import deque  # use deck to moreeffective (faster) works with animations
from ray_casting import mapping
from numba.core import types
from numba.typed import Dict   # numba doesn't support standard pythonic dict
from numba import int32


class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'sprite_barrel': {
                'sprite': pygame.image.load('sprites/barrel/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'side': 30,
                'animation': deque(
                    [pygame.image.load(f'sprites/barrel/anim/{i}.png').convert_alpha() for i in range(12)]),
                'death_animation': deque([pygame.image.load(f'sprites/barrel/death/{i}.png')
                                          .convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 2.6,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'decor',
                'obj_action': []
            },
            'sprite_pin': {
                'sprite': pygame.image.load('sprites/pin/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque([pygame.image.load(f'sprites/pin/anim/{i}.png').convert_alpha() for i in range(8)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': None,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'decor',
                'obj_action': []
            },
            'sprite_flame': {
                'sprite': pygame.image.load('sprites/flame/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque(
                    [pygame.image.load(f'sprites/flame/anim/{i}.png').convert_alpha() for i in range(16)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 1.8,
                'animation_dist': 1800,
                'animation_speed': 5,
                'blocked': None,
                'flag': 'decor',
                'obj_action': []
            },
            'npc_devil0': {
                'sprite': [pygame.image.load(f'sprites/npc/devil0/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.0,
                'scale': (1.1, 1.1),
                'side': 50,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/devil0/death/{i}.png')
                                           .convert_alpha() for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'animation_dist': None,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque(
                    [pygame.image.load(f'sprites/npc/devil0/anim/{i}.png').convert_alpha() for i in range(9)]),
            },
            'npc_devil1': {
                'sprite': [pygame.image.load(f'sprites/npc/devil1/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.0,
                'scale': (1.1, 1.1),
                'side': 50,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/devil1/death/{i}.png')
                                         .convert_alpha() for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'animation_dist': None,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque(
                    [pygame.image.load(f'sprites/npc/devil1/anim/{i}.png').convert_alpha() for i in range(6)]),
            },
            'sprite_door_v': {
                'sprite': [pygame.image.load(f'sprites/doors/door_v/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_h',
                'obj_action': []
            },
            'sprite_door_h': {
                'sprite': [pygame.image.load(f'sprites/doors/door_h/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_v',
                'obj_action': []
            },
            'npc_soldier0': {
                'sprite': [pygame.image.load(f'sprites/npc/soldier0/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.8,
                'scale': (0.4, 0.6),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/soldier0/death/{i}.png')
                                         .convert_alpha() for i in range(10)]),
                'is_dead': None,
                'dead_shift': 1.7,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/soldier0/action/{i}.png')
                                    .convert_alpha() for i in range(4)])
            },
            'npc_soldier1': {
                'sprite': [pygame.image.load(f'sprites/npc/soldier1/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.8,
                'scale': (0.4, 0.6),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/soldier1/death/{i}.png')
                                         .convert_alpha() for i in range(10)]),
                'is_dead': None,
                'dead_shift': 1.7,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/soldier1/action/{i}.png')
                                    .convert_alpha() for i in range(4)])
            }
        }

        # all sprites in the map
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['sprite_barrel'], (7.1, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (5.9, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (18.5, 2.3)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (8.7, 2.5)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (16.1, 10.0)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (15.8, 10.0)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (18.5, 2.5)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (17.5, 3.5)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (23.0, 13.5)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (23.0, 14.5)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (21.4, 15.0)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (22.0, 14.5)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (7, 2.8)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (13.0, 8.0)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (19.8, 14.1)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (12.3, 9.5)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (8.6, 5.6)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (21.5, 13.9)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (18.1, 14.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (3.5, 3.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (13.5, 10.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (13.5, 12.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (9.5, 7.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (17.5, 14.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (1.5, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (22.5, 11.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (2.5, 1.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (5.51, 1.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (6.61, 3.92)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (7.68, 1.47)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (8.75, 3.65)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (1.27, 11.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (1.26, 8.29)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (21.5, 1.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (21.5, 5.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (19.8, 15.0)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (4.5, 10.0)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (3.5, 10.0)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (13.1, 2.0)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (12.1, 14.5)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (19.5, 10.5)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (18.1, 14.0))
        ]

    @property
    def sprite_shot(self):
        """
        Returns sprite if there are many sprites reached be the shot
        :return:
        """
        return min([obj.is_on_fire for obj in self.list_of_objects], default=(float('inf'), 0))

    @property
    def blocked_doors(self):
        """
        All closed doors on the map
        :return:
        """
        blocked_doors = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
        for obj in self.list_of_objects:
            if obj.flag in {"door_h", "door_v"} and obj.blocked:
                i, j = mapping(obj.x, obj.y)
                blocked_doors[(i, j)] = 0
        return blocked_doors


class SpriteObject:
    def __init__(self, parameters, pos):
        """
        :param object: sprite type
        :param static: is sprite static picture without angles of view?
        :param pos: position on map
        :param shift: vertical shift
        :param scale: масштабирование
        """
        self.dead_sprite = None
        self.theta = 0
        self.distance_to_sprite = 0
        self.current_ray = 0
        self.proj_height = 0
        self.object = parameters['sprite'].copy()  # necessarily use copy to prevent animation bugs
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        # ---------------------
        self.death_animation = parameters['death_animation'].copy()
        self.is_dead = parameters['is_dead']
        self.dead_shift = parameters['dead_shift']
        # ---------------------
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.flag = parameters['flag']
        self.obj_action = parameters['obj_action'].copy()
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.side = parameters['side']   # square side, where sprite will be put
        self.dead_animation_count = 0
        self.animation_count = 0
        self.npc_action_trigger = False
        self.door_prev_pos = self.y if self.flag == 'door_h' else self.x
        self.delete = False
        self.door_open_trigger = False
        # previous door position (for its opening animation)
        self.door_prev_pos = self.y if self.flag == "door_h" else self.x
        # attribute for object deletion
        self.delete = False
        # for dynamic sprites
        if self.viewing_angles:
            # set range of the angles for every sprite
            # e.g. if sprite has 8 pics, every sprite uses range of the 45 degrees angles
            # using frozenset for fast search of the dict keys
            # sets cannot be dict keys due to its mutability
            if len(self.object) == 8:
                self.sprite_angles = [frozenset(range(338, 361)) | frozenset(range(0, 23))] + \
                                     [frozenset(range(i, i + 45)) for i in range(23, 338, 45)]
            # 16 angles for doors:
            else:
                self.sprite_angles = [frozenset(range(348, 361)) | frozenset(range(0, 11))] + \
                                     [frozenset(range(i, i + 23)) for i in range(11, 348, 23)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    @property
    def is_on_fire(self):
        """ Returns proj sprite distance, that is on fire
            (in the central ray and in a few rays next to it) """
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
            return self.distance_to_sprite, self.proj_height
        return float('inf'), None

    @property
    def pos(self):
        """ adjusting the position of the square (in the center of the sprite) """
        return self.x - self.side // 2, self.y - self.side // 2

    def object_locate(self, player):
        """
        Calculate distance between player and sprite
        :param player: player
        :param walls: dict with numbers of rays distances to walls
        :return:
        """
        # # fix issue: any sprite disappears when its middle part hides behind the edge of the screen
        # # adding fake rays, to make sprite smoothly abandon the edge of the screen
        # fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]
        # fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]
        # fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI
        self.theta -= 1.4 * gamma  # adjust calculating the angle for more correct sprite display

        # sprite shift regarding the central ray
        delta_rays = int(gamma / DELTA_ANGLE)
        self.current_ray = CENTER_RAY + delta_rays
        # condition for doors
        if self.flag not in {"door_h", "door_v"}:
            # adjust the distance to the sprite to avoid the "fish-eye" effect
            self.distance_to_sprite *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS
        # check if the ray with sprite matches the rays range
        # if the ray matches obstacles: also check if the sprite will be closer than the wall
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            # sprite projection height
            # to prevent decreasing fps while comping to sprites, restrict its projection size
            self.proj_height = min(int(PROJ_COEFF / self.distance_to_sprite),
                                   DOUBLE_HEIGHT if self.flag not in {"door_h", "door_v"} else HEIGHT)

            # adjustments for correct scaling along the X and Y axes
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            # sprite scale coefficient
            half_sprite_height = sprite_height // 2
            # sprite shift along the Y-axis (to scale any sprite without distorting its original proportions)
            # in other words: sprite height adjustment mechanism
            shift = half_sprite_height * self.shift

            # logic for doors, npc, decor
            if self.flag in {"door_h", "door_v"}:
                if self.door_open_trigger:
                    self.open_door()
                self.object = self.visible_sprite()
                sprite_object = self.sprite_animation()
            else:
                # logic for death animation and npc interaction animation
                if self.is_dead and self.is_dead != "immortal":
                    sprite_object = self.dead_animation()
                    shift = half_sprite_height * self.dead_shift
                    sprite_height = int(sprite_height / 1.3)
                elif self.npc_action_trigger:
                    sprite_object = self.npc_in_action()
                else:
                    self.object = self.visible_sprite()
                    sprite_object = self.sprite_animation()

            # sprite scale and pos
            # sprite position regarding its ray
            # to do this, correlate the center of the sprite with its ray...
            # and determine the position regarding the height, taking into account the specified shift
            sprite_pos = (self.current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)
            # scale the sprite regarding its projection size
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            return (self.distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)

    def sprite_animation(self):
        if self.animation and self.distance_to_sprite < self.animation_dist:
            sprite_object = self.animation[0]  # display first sprite in deque
            if self.animation_count < self.animation_speed:
                self.animation_count += 1
            # when self.animation_count == self.animation_speed:
            else:
                self.animation.rotate()
                self.animation_count = 0
            return sprite_object
        return self.object

    def visible_sprite(self):
        """
        Определение правильного угла обзора для спрайта
        :return:
        """
        # choosing dynamic sprite for angle theta
        if self.viewing_angles:
            # adjust the theta angle to put it within [0, 2pi]
            if self.theta < 0:
                self.theta += DOUBLE_PI
            self.theta = 360 - int(math.degrees(self.theta))

            for angles in self.sprite_angles:
                # as soon as theta matches with one of the ranges:
                if self.theta in angles:
                    # required sprite is the value retrieved by this angle key
                    return self.sprite_positions[angles]
        return self.object

    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    def npc_in_action(self):
        sprite_object = self.obj_action[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1
        else:
            self.obj_action.rotate()
            self.animation_count = 0
        return sprite_object

    def open_door(self):
        if self.flag == "door_h":
            self.y -= 3
            if abs(self.y - self.door_prev_pos) > TILE:
                self.delete = True
        elif self.flag == "door_v":
            self.x -= 3
            if abs(self.x - self.door_prev_pos) > TILE:
                self.delete = True
