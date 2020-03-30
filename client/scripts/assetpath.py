#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : assetpath.py
# @Time : 2020/3/30 17:51 
# @GitHub: https://github.com/hittun/pygamel
"""
import os


def get_asset_root():
    return os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "assets")


def get_asset_map(filename="map.jpg"):
    return os.path.join(get_asset_root(), "map", filename)


def get_asset_music(filename="bgmusic.mp3"):
    return os.path.join(get_asset_root(), "music", filename)


def get_asset_char(filename="bluesquare.png"):
    return os.path.join(get_asset_root(), "char", filename)

