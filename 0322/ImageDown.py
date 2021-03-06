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


def down_image(img_url, base_path='down/', batch_size=1, sleep_time=5):
    print("ready down image from url")
    for i in range(batch_size):
        time.sleep(sleep_time)
        img = requests.get(img_url, stream=True)
        with open(base_path + g_rand_file_name('jpeg'), 'ab') as f:
            f.write(img.content)
            f.close()
    print("down image from url end")


def g_rand_file_name(type):
    file_name = ''
    for i in range(16):
        file_name = file_name + chr(random.randint(65, 90))
        file_name = file_name + chr(random.randint(48, 57))
    return file_name + '.' + type


# 160，70
def split_image(filename, base_path='down/', split_size=4, target_path='split/'):
    im = Image.open(base_path + filename)
    width = im.size[0]
    height = im.size[1]
    max_color_x_coordinate = get_color_coordinate(filename, base_path)
    rgb_im = im.convert('RGB')

    file_base_name = filename.split('.')[0]

    rgb_im.crop((0, 0, max_color_x_coordinate[2], height)).save(target_path + file_base_name + "p1.jpeg")  # 160，70

    rgb_im.crop((max_color_x_coordinate[1], 0, max_color_x_coordinate[4], height)).save(
        target_path + file_base_name + "p2.jpeg")  # 160，70

    rgb_im.crop((max_color_x_coordinate[3], 0, max_color_x_coordinate[6], height)).save(
        target_path + file_base_name + "p3.jpeg")  # 160，70

    rgb_im.crop((max_color_x_coordinate[5], 0, width, height)).save(target_path + file_base_name + "p4.jpeg")  # 160，70


def coverL(filename, base_path='split/', target_path='gray/'):
    im = Image.open(base_path + filename).convert('L')
    im.save(target_path + filename)


def flow():
    down_base = 'down/'
    split_base = 'split/'
    gray_base = 'gray/'
    down_url = 'http://shixin.court.gov.cn/captcha.do'

    if os.path.exists(down_base):
        # shutil.rmtree(down_base)
        print("清理文件开始")
        shutil.rmtree(split_base)
        shutil.rmtree(gray_base)
        print("清理文件开始")
    # os.mkdir(down_base)
    print("创建文件开始")
    os.mkdir(split_base)
    os.mkdir(gray_base)
    print("创建文件结束")

    # down_image(down_url, batch_size=2000, sleep_time=2)

    down_images = [f for f in listdir(down_base) if isfile(join(down_base, f))]
    for file in down_images:
        split_image(filename=file)

    split_files = [f for f in listdir(split_base) if isfile(join(split_base, f))]
    for file in split_files:
        coverL(filename=file)


def get_color_coordinate(file_name, base_path):
    im = Image.open(base_path + file_name)
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
    max_color_x_coordinate = []
    for max_four_color in max_four:
        max_color.append(max_four_color[0])
        max_color_coordinate[max_four_color[0]] = [];
        max_color_min_max[max_four_color[0]] = [];

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
        max_color_x_coordinate.append(min(v))
        max_color_x_coordinate.append(max(v))
    max_color_x_coordinate.sort()
    return max_color_x_coordinate


if __name__ == "__main__":
    flow()
