#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
辅助（Support）：
    俗称SUP，辅助类英雄的能力是透过治疗队友、牵制对手等方式来辅佐团队，
    辅助在游戏早期通常会与射手英雄搭配，并试图让与他搭配的队友尽可能地生存下去，
    偶尔还必须骚扰对手。辅助的另一个重要工作是提供团队更大的视野。
# @File : support.py
# @Time : 2020/3/28 4:49 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Support(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ZhuangZhou(Support):
    """庄周"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



