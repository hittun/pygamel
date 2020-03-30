#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : base.py
# @Time : 2020/3/30 19:33 
# @GitHub: https://github.com/hittun/pygamel
"""
import pygame
from ..component import Transform
from ..component import Audio
from ..component import SpriteRenderer
from ..esper import Processor


g_Window = None

RESOLUTION = 530, 300


def get_window():
    global g_Window
    if not g_Window:
        g_Window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Hello Game")
    return g_Window



class AudioProcessor(Processor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, *args, **kwargs):
        cls = Audio
        for ent, audio in self.world.get_component(cls):
            if audio.state == cls.STATE_START:
                pygame.mixer.init()
                pygame.mixer.music.load(audio.filepath)
                pygame.mixer.music.play(-1)
                audio.state = cls.STATE_RUNNING


class SpriteProcessor(Processor):
    def __init__(self, clear_color=(0, 0, 0)):
        super().__init__()
        self.clear_color = clear_color

    def process(self, *args, **kwargs):
        window = get_window()
        for ent, (transform, rend) in self.world.get_components(Transform, SpriteRenderer):
            cls = type(rend)
            if rend.state == cls.STATE_LOAD:
                rend.image = pygame.image.load(rend.filepath)
                rend.state = cls.STATE_LOADED
                # w = rend.image.get_width()
                # h = rend.image.get_height()
                # window = pygame.display.set_mode((w, h))
            window.blit(rend.image, (transform.position.x, transform.position.y))
        pygame.display.update()



class BaseEventProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, *args, **kwargs):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if running is False:
            pygame.quit()