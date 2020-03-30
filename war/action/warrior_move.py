#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : warrior_move.py
# @Time : 2020/3/28 18:42 
# @GitHub: https://github.com/hittun/pygamel
"""
from ecs import Component
from ecs import Processor


class WarriorTransformChange(Component):
    pass


# class WarriorMoveProcessor(Processor):
#
#     def process(self, *args, **kwargs):
#         for ent, (nowTrans, chgTrans, rand) in self.world.get_components(NowTransform, ChgTransform, SpriteRenderer):
#             new_position = nowTrans.position + chgTrans.position
#             new_position.x = max(self.minx, new_position.x)
#             new_position.x = min(self.maxx - rand.image.get_width(), new_position.x)
#             new_position.y = max(self.miny, new_position.y)
#             new_position.y = min(self.maxy - rand.image.get_height(), new_position.y)
#             nowTrans.position = new_position