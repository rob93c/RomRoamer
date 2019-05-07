[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d98aee71611a42dba0b510d5639b6aa3)](https://www.codacy.com/app/rob93c/RomRoamer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rob93c/RomRoamer&amp;utm_campaign=Badge_Grade)![GitHub top language](https://img.shields.io/github/languages/top/rob93c/RomRoamer.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2UIWJ)

# RomRoamer

Use this script to roam in squares inside a ROM game, for instance Pokémon Red.
The program works with every emulator using arrow keys to move around (GB/GBA/NDS games are supported).

## Instructions

First make sure you have installed [`python3`](https://www.python.org/downloads/).
Open the game and place yourself in an open area (at least 9x9).
At this point launch the script in the terminal browsing to its path and then use 
`python3`[`RomRoamer.py`](https://github.com/rob93c/RomRoamer/blob/master/RomRoamer.py)
You now have 3 seconds to switch to the emulator's window so the program can let you wander around.
Keep in mind that this only works if you keep the emulator's window opened and in the foreground.

Feel free to adapt the script to your needs, I.E. if you need to run along a vertical line just remove or comment `Go left` and `Go right` chunks.


### License

See the [LICENSE](https://github.com/rob93c/RomRoamer/blob/master/LICENSE.md) file for license rights and limitations (MIT).