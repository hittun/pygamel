#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
战士（Fighter）：
    战士是能输出伤害的坦克，相较于坦克，战士的攻击力较高但生命值较低；
    相较于刺客，战士的攻击力较低而生命值较高。
# @File : fighter.py
# @Time : 2020/3/28 4:48 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Fighter(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class XiangYu(Fighter):
    """项羽"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

