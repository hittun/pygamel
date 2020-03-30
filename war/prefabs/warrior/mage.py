#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
法师（Mage）：
    法师俗称AP或APC，是具有强大魔法伤害技能、但防守能力和移动能力偏低的英雄。
    一些法师可以在短时间内造成巨大伤害，一些则是以长期持续伤害为主，爆发性的法师和刺客间的界线很模糊。
# @File : mage.py
# @Time : 2020/3/28 4:46 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Mage(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DaJi(Mage):
    """妲己"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


