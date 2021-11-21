from PIL import ImageGrab
import pyautogui
import colorsys


def get_pixel_colour(i_x, i_y):
    return ImageGrab.grab().load()[i_x, i_y]


mouse = list(pyautogui.position())
r, g, b = [i for i in list(get_pixel_colour(mouse[0], mouse[1]))]
hls = list(colorsys.rgb_to_hls(r/255, g/255, b/255))
print(round((hls[0]*360)), round((hls[2]*100)), round((hls[1]*100)))
