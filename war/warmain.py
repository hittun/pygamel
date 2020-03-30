#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : warmain.py
# @Time : 2020/3/28 5:12 
# @GitHub: https://github.com/hittun/pygamel
"""

################################
#  The main core of the program:
################################
from public import Vec3
from ecs import Transform
from .warworld import get_world
from .prefabs import *


def init():
    world = get_world()
    main_scene = world.create_entity()
    world.add_prefab(main_scene, ScenePrefab())


def start():
    world = get_world()
    # player
    player1 = world.create_entity()
    player2 = world.create_entity()
    player3 = world.create_entity()

    world.add_prefab(player1, LiBai(Transform(position=Vec3(100, 200, 0))))
    world.add_prefab(player2, LianPo(Transform(position=Vec3(200, 200, 0))))
    world.add_prefab(player3, HouYi(Transform(position=Vec3(300, 200, 0))))

    # enemy
    enemy1 = world.create_entity()
    enemy2 = world.create_entity()
    enemy3 = world.create_entity()

    world.add_prefab(enemy1, LiBai(Transform(position=Vec3(100, 0, 0))))
    world.add_prefab(enemy2, LianPo(Transform(position=Vec3(200, 0, 0))))
    world.add_prefab(enemy3, HouYi(Transform(position=Vec3(300, 0, 0))))


def loop():
    world = get_world()
    world.process()

    return False