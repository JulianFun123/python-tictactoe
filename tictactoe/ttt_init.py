#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# Intro Animation steps


intro_step_1 = """
  ▀█▀ ▀ ▄▀
  ░█░ █ █░
  ░▀░ ▀ ░▀
"""

intro_step_2 = """
  ▀█▀ ▀ ▄▀ ▀█▀ ▄▀▄ ▄▀
  ░█░ █ █░ ░█░ █▀█ █░
  ░▀░ ▀ ░▀ ░▀░ ▀░▀ ░▀
"""

intro_step_3 = """
  ▀█▀ ▀ ▄▀ ▀█▀ ▄▀▄ ▄▀ ▀█▀ ▄▀▄ █▀▀
  ░█░ █ █░ ░█░ █▀█ █░ ░█░ █░█ █▀▀
  ░▀░ ▀ ░▀ ░▀░ ▀░▀ ░▀ ░▀░ ░▀░ ▀▀▀
"""



def flyingMatchfield():
    print(" 1|2|3")
    time.sleep(0.05)
    print(" 4|5|6")
    time.sleep(0.05)
    print(" 7|8|9")
    time.sleep(3)
    print("\n"*100)
