#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pynput.keyboard import Key, Controller
from time import sleep

"""
RomRoamer: automatically wander playing with 
	   a GBC/GBA/NDS rom (E.G. to hatch
	   eggs in Pokémon games or level up 
	   a Pokémon left at the Day Care).
"""


class RomRoamer:

    def __init__(self) -> None:
        self.times = int(
            input("\nHow many times do you want to roam in a square? "))

    def roam(self) -> None:
        try:
            keyboard = Controller()
            sleep(3)
            while self.times > 0:

                # Go down
                keyboard.press(Key.down)
                sleep(0.8)
                keyboard.release(Key.down)

                # Go right
                keyboard.press(Key.right)
                sleep(0.8)
                keyboard.release(Key.right)

                # Go up
                keyboard.press(Key.up)
                sleep(0.8)
                keyboard.release(Key.up)

                # Go left
                keyboard.press(Key.left)
                sleep(0.8)
                keyboard.release(Key.left)

                self.times -= 1

        except ValueError as e:
            msg = "Insert a valid number.\n{}: {}".format(type(e).__name__, e)
            print(msg)

go = RomRoamer()
go.roam()
