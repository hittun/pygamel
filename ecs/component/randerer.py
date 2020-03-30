#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Render related, only the client concerns, the server environment will not enter any rendering logic
# @File : randerer.py
# @Time : 2020/3/28 3:38 
# @GitHub: https://github.com/hittun/pygamel
"""
from ecs.component.base import Renderer


class SpriteRenderer(Renderer):
    """Class like Unity Component SpriteRenderer"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = None
