#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : scene.py
# @Time : 2020/3/30 19:24 
# @GitHub: https://github.com/hittun/pygamel
"""
from ecs import Perfab

from ecs import SpriteRenderer
from ecs import Audio

from ecs import SpriteProcessor
from ecs import AudioProcessor
from ecs import BaseEventProcessor


from client.scripts import assetpath


class ScenePrefab(Perfab):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_scene_prefab()

    def init_scene_prefab(self):
        # component ----------------------
        # 背景
        cls = SpriteRenderer
        filepath = assetpath.get_asset_map("map.jpg")
        sprite = cls(filepath=filepath)
        sprite.state = cls.STATE_LOAD
        self.add_component(sprite)
        # 音乐
        cls = Audio
        filepath = assetpath.get_asset_music("bgmusic.mp3")
        audio = cls(filepath=filepath)
        audio.state = cls.STATE_START
        self.add_component(audio)

        # system ----------------------
        sp = SpriteProcessor()
        self.add_processor(sp)
        ap = AudioProcessor()
        self.add_processor(ap)
        self.add_processor(BaseEventProcessor())
