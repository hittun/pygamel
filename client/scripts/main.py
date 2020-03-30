#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @File : main.py
# @Time : 2020/3/30 15:35 
# @GitHub: https://github.com/hittun/pygamel
"""
import pygame
clock = pygame.time.Clock()

FPS = 1


def start():
    from war.warmain import init as func_war_init
    from war.warmain import start as func_war_start
    from war.warmain import loop as func_war_loop

    pygame.init()
    func_war_init()
    func_war_start()
    running = True
    while running:
        res = func_war_loop()
        if res:
            running = False
        clock.tick(FPS)
    pygame.quit()
