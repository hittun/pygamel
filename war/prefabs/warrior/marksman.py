#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
射手（Marksman）：
    射手俗称ADC或AD，是主要造成远程物理伤害的英雄，
    这些英雄有较高的每秒伤害（DPS）而不是爆发能力，他们通常是破坏防御塔的主力，
    不过他们的防御力偏低，容易遭到火力瞄准。
# @File : marksman.py
# @Time : 2020/3/28 4:46 
# @GitHub: https://github.com/hittun/pygamel
"""
from .warrior import Warrior


class Marksman(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HouYi(Marksman):
    """后羿"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


