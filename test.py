"""from PIL import ImageChops
from pyscreenshot import grab


def get_pixel_colour(x, y):
    ib = grab(bbox=(486, 517, 487, 518))
    ib.show()
    im = grab(bbox=(486, 517, 487, 518)).load()[x, y]
    return im


print(get_pixel_colour(487, 518))
"""
import pyautogui

pyautogui.keyDown('win')
pyautogui.press('up')
pyautogui.keyUp('win')