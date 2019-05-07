from pynput.keyboard import Key, Controller
from time import sleep

"""
RomRoamer: automatically wander playing with 
	   a GBC/GBA/NDS rom. (E.G. to hatch
	   eggs in Pokémon games or level up 
	   a Pokémon left at the Day Care)
"""


class RomRoamer(object):

    def roam(times: int):
        keyboard = Controller()
        sleep(3)
        for i in range(times):

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


    num = input("How many times do you want to roam in a square? ")
    roam(int(num))
