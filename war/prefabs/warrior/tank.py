#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
坦克（Tank）：
    坦克是难以被杀死的英雄，他们有着高防御、高生命值或高护盾。
    不过他们的伤害偏低。有些坦克具有控场能力，可以迫使敌人分散或使敌人僵直，也能迫使敌人攻击自己。
# @File : tank.py
# @Time : 2020/3/28 4:48 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Tank(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LianPo(Tank):
    """廉颇"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



