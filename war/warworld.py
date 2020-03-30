#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : warworld.py
# @Time : 2020/3/28 5:21 
# @GitHub: https://github.com/hittun/pygamel
"""
from ecs import World


g_World = None


def get_world():
    global g_World
    if not g_World:
        g_World = World()
    return g_World
