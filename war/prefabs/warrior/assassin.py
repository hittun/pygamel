#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
刺客（Assassin）：
    刺客是专精于迅速地杀死另一个英雄的英雄。
    这些英雄往往会追着对方的射手和法师跑，因为他们的防御力较差。
    虽然刺客的防御也不怎么高，但他有着迅速移动的能力。
    刺客的攻击依赖的是短时间内的瞬间伤害，在攻击结束之后，他们会比较虚弱。
# @File : assassin.py
# @Time : 2020/3/28 4:47 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Assassin(Warrior):
    """Assassin base class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LiBai(Assassin):
    """李白"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
