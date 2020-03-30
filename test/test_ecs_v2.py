#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : test_ecs_v2.py
# @Time : 2020/3/27 17:25 
# @GitHub: https://github.com/hittun/pygamel
"""

import pygame
from public import Vec3
from ecs import World
from ecs import Processor
from ecs import Transform
from ecs import SpriteRenderer

FPS = 60
RESOLUTION = 720, 480


def get_filepath(filename):
    import os
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


################################
#  Define some Processors:
################################
class NowTransform(Transform):
    pass


class ChgTransform(Transform):
    pass


################################
#  Define some Processors:
################################


class MovementProcessor(Processor):
    def __init__(self, minx, maxx, miny, maxy):
        super().__init__()
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def process(self):
        for ent, (nowTrans, chgTrans, rand) in self.world.get_components(NowTransform, ChgTransform, SpriteRenderer):
            new_position = nowTrans.position + chgTrans.position
            new_position.x = max(self.minx, new_position.x)
            new_position.x = min(self.maxx - rand.image.get_width(), new_position.x)
            new_position.y = max(self.miny, new_position.y)
            new_position.y = min(self.maxy - rand.image.get_height(), new_position.y)
            print(nowTrans.position, chgTrans.position, new_position)
            nowTrans.position = new_position


class RenderProcessor(Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        # Clear the window:
        self.window.fill(self.clear_color)
        # This will iterate over every Entity that has this Component, and blit it:
        for ent, (transform, rend) in self.world.get_components(NowTransform, SpriteRenderer):
            self.window.blit(rend.image, (transform.position.x, transform.position.y))
        # Flip the framebuffers
        pygame.display.flip()


################################
#  The main core of the program:
################################
def run():
    # Initialize Pygame stuff
    pygame.init()
    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Pygame example")
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    # Initialize world, and create a "player" Entity with a few Components.
    world = World()
    player = world.create_entity()
    world.add_component(player, NowTransform(position=Vec3(200, 200, 0)))
    world.add_component(player, ChgTransform())
    world.add_component(player, SpriteRenderer(image=pygame.image.load(get_filepath(
        "../client/assets/char/redsquare.png"))))
    # Another motionless Entity:
    enemy = world.create_entity()
    world.add_component(enemy, NowTransform(position=Vec3(400, 200, 0)))
    world.add_component(enemy, SpriteRenderer(image=pygame.image.load(get_filepath(
        "../client/assets/char/bluesquare.png"))))

    # Create some Processor instances, and asign them to be processed.
    render_processor = RenderProcessor(window=window)
    world.add_processor(render_processor)
    movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])
    world.add_processor(movement_processor, priority=1)
    running = True
    while running:
        # Processing user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Here is a way to directly access a specific Entity's
                    # Transform Component's attribute (y) without making a
                    # temporary variable.
                    world.component_for_entity(player, ChgTransform).position.x = -3
                elif event.key == pygame.K_RIGHT:
                    world.component_for_entity(player, ChgTransform).position.x = 3
                elif event.key == pygame.K_UP:
                    world.component_for_entity(player, ChgTransform).position.y = -3
                elif event.key == pygame.K_DOWN:
                    world.component_for_entity(player, ChgTransform).position.y = 3
                elif event.key == pygame.K_SPACE:
                    world.component_for_entity(player, ChgTransform).position.y = -10
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    world.component_for_entity(player, ChgTransform).position.x = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    world.component_for_entity(player, ChgTransform).position.y = 0
                elif event.key in (pygame.K_SPACE, ):
                    world.component_for_entity(player, ChgTransform).position.y = 10

        # A single call to world.process() will update all Processors:
        world.process()

        clock.tick(60)


if __name__ == "__main__":
    run()
    pygame.quit()

