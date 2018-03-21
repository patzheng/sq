# 批量下载验证码
import requests
import os
from os.path import isfile, join
from os import listdir
import random
import time
from PIL import Image
import shutil
import collections
import matplotlib.pyplot as plt


def imageRegex():
    im = Image.open('down/X7U9O2U7L5X8U8G5H3N6S4S1V2V4I4A6.jpeg')
    rgb_count = []
    im = im.convert('RGB')
    width = im.size[0]
    height = im.size[1]
    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            if r < 255 and r > 240 and g < 255 and g > 240 and b < 255 and g > 240:
                r = 255
                g = 255
                b = 255
            if r == 255 and g == 255 and b == 255:
                continue
            else:
                rgb = (str(r) + ',' + str(g) + ',' + str(b))
                rgb_count.append(rgb)
    m = collections.Counter(rgb_count)
    max_four = m.most_common(4)
    max_color = []
    max_color_coordinate = {}
    max_color_min_max = {}
    for max_four_color in max_four:
        max_color.append(max_four_color[0])
        max_color_coordinate[max_four_color[0]] = [];
        max_color_min_max[max_four_color[0]] = [];

    print(max_color_coordinate)
    width = im.size[0]
    height = im.size[1]
    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            if r < 255 and r > 240 and g < 255 and g > 240 and b < 255 and g > 240:
                r = 255
                g = 255
                b = 255
            if r == 255 and g == 255 and b == 255:
                continue
            else:
                rgb = (str(r) + ',' + str(g) + ',' + str(b))
                if rgb in max_color:
                    max_color_coordinate[rgb].append(i)
    for k, v in max_color_coordinate.items():
        max_color_min_max[k].append(min(v))
        max_color_min_max[k].append(max(v))
    print(max_color_min_max)



if __name__ == "__main__":
    imageRegex()
