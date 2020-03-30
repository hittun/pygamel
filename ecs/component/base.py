#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : base.py
# @Time : 2020/3/27 18:45 
# @GitHub: https://github.com/hittun/pygamel
"""
from public import Vec3
from ecs.gameobject import GameObject


class Component(GameObject):
    """Class from which all components should derive."""
    pass


class Transform(Component):
    """Class like Unity Component Transform"""

    def __init__(self, position=None, rotation=None, scale=None):
        if position is None:
            position = Vec3()
        if rotation is None:
            rotation = Vec3()
        if scale is None:
            scale = Vec3()
        self._position = position
        self._rotation = rotation
        self._scale = scale

    def reset(self) -> None:
        """Reset Attrs"""
        self._position = Vec3()
        self._rotation = Vec3()
        self._scale = Vec3()

    position = property(lambda self: self._position, lambda self, v: setattr(self, "_position", v),
                        lambda self: delattr(self, "_position"))

    rotation = property(lambda self: self._position, lambda self, v: setattr(self, "_rotation", v),
                        lambda self: delattr(self, "_rotation"))

    scale = property(lambda self: self._position, lambda self, v: setattr(self, "_scale", v),
                     lambda self: delattr(self, "_scale"))


class Script(Component):
    """User Script, The code that handles the logic"""
    pass


class Renderer(Component):
    """Render related, only the client concerns, the server environment will not enter any rendering logic"""
    STATE_UNLOAD = 0
    STATE_LOAD = 1
    STATE_LOADED = 2

    def __init__(self, filepath, depth=0):
        super().__init__()
        self._filepath = filepath
        self._depth = depth
        self._state = 0

    filepath = property(lambda self: getattr(self, "_filepath", None), lambda self, v: setattr(self, "_filepath", v),
                        lambda self: delattr(self, "_filepath"))

    depth = property(lambda self: getattr(self, "_depth", None), lambda self, v: setattr(self, "_depth", v),
                     lambda self: delattr(self, "_depth"))

    state = property(lambda self: getattr(self, "_state", None), lambda self, v: setattr(self, "_state", v),
                     lambda self: delattr(self, "_state"))


class Physics(Component):
    """Physical engine base class"""
    pass


class UI(Component):
    """UI system base class, client concerns"""
    pass


class Navigation(Component):
    """The navigation path finding"""
    pass


class Effects(Component):
    """Some effects, client concerns"""
    pass


class Audio(Component):
    """Sounds, client concerns"""
    STATE_START = 0
    STATE_RUNNING = 1
    STATE_QUIP = 2

    def __init__(self, filepath):
        self._state = type(self).STATE_START
        self._filepath = filepath

    state = property(lambda self: getattr(self, "_state", None), lambda self, v: setattr(self, "_state", v),
                     lambda self: delattr(self, "_state"))
    filepath = property(lambda self: getattr(self, "_filepath", None), lambda self, v: setattr(self, "_filepath", v),
                        lambda self: delattr(self, "_filepath"))


class Map(Component):
    """Map system"""
    pass
