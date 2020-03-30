#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : warrior.py
# @Time : 2020/3/28 4:51 
# @GitHub: https://github.com/hittun/pygamel
"""
from ecs import Perfab
from ecs import PrefabRender
from ecs import SpriteRenderer
from ecs import SpriteProcessor

from client.scripts import assetpath


class Warrior(Perfab):
    _user_id = None
    _user_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_warrior()

    def init_warrior(self):
        cls = SpriteRenderer
        filepath = assetpath.get_asset_char()
        sprite = cls(filepath=filepath)
        sprite.state = cls.STATE_LOAD
        self.add_component(sprite)
        self.add_processor(SpriteProcessor())
