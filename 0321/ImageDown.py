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

    rgb_im.crop((0, 0, max_color_x_coordinate[2], height)).save(target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((max_color_x_coordinate[1], 0, max_color_x_coordinate[4], height)).save(
        target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((max_color_x_coordinate[3], 0, max_color_x_coordinate[6], height)).save(
        target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((max_color_x_coordinate[5], 0, width, height)).save(target_path + g_rand_file_name('jpeg'))  # 160，70


def coverL(filename, base_path='split/', target_path='gray/'):
    im = Image.open(base_path + filename).convert('L')
    im.save(target_path + g_rand_file_name('jpeg'))


def flow():
    down_base = 'down/'
    split_base = 'split/'
    gray_base = 'gray/'
    down_url = 'http://shixin.court.gov.cn/captcha.do'

    if os.path.exists(down_base):
        # shutil.rmtree(down_base)
        shutil.rmtree(split_base)
        shutil.rmtree(gray_base)

    # os.mkdir(down_base)
    os.mkdir(split_base)
    os.mkdir(gray_base)

    down_image(down_url, batch_size=2000, sleep_time=2)

    down_images = [f for f in listdir(down_base) if isfile(join(down_base, f))]
    for file in down_images:
        print(file)
        split_image(filename=file)

    split_files = [f for f in listdir(split_base) if isfile(join(split_base, f))]
    for file in split_files:
        coverL(filename=file)


def get_color_coordinate(file_name, base_path, max_color_number=4):
    im = Image.open(base_path + file_name)

    image_rgb_collection = []
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
                image_rgb_collection.append(rgb)
    m = collections.Counter(image_rgb_collection)
    print(m)

    max_four = m.most_common(max_color_number)
    print(max_four)

    max_color = []
    max_color_coordinate = {}
    max_color_min_max = {}

    for max_four_color in max_four:
        max_color.append(max_four_color[0])
        max_color_coordinate[max_four_color[0]] = [];
        max_color_min_max[max_four_color[0]] = [];

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

    max_color_x_coordinate = []
    for k, v in max_color_coordinate.items():
        max_color_min_max[k].append(min(v))
        max_color_min_max[k].append(max(v))
        max_color_x_coordinate.append(min(v))
        max_color_x_coordinate.append(max(v))
    max_color_x_coordinate.sort()
    print('x_coordinate:', max_color_x_coordinate)
    return max_color_x_coordinate


def get_color_coordinate_new(file_name, base_path, max_color_number=4):
    # 打开图片
    im = Image.open(base_path + file_name)
    # 从四通道转单通道
    im = im.convert('RGB')
    # 图片宽度
    width = im.size[0]
    # 图片高度
    height = im.size[1]

    # 颜色对应的数量
    image_rgb_str_collection = []

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
                image_rgb_str_collection.append(rgb)

    # 得到最大的四个像素的RGB逗号组装的 字符串 和 数量
    max_color_count_dict = collections.Counter(image_rgb_str_collection).most_common(max_color_number + 4)

    print('max_four', max_color_count_dict)

    max_more_like = {}
    for max_color_count_ele in max_color_count_dict:
        rgb_str = max_color_count_ele[0]
        rgb = rgb_str.split(',')
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        r_max = int(r) + 5
        r_min = int(r) - 5

        g_max = int(g) + 5
        g_min = int(g) - 5

        b_max = int(b) + 5
        b_min = int(b) - 5

        for i in range(r_min, r_max):
            for j in range(g_min, g_max):
                for k in range(b_min, b_max):
                    rgb = (str(i) + ',' + str(j) + ',' + str(k))
                    max_more_like[rgb] = rgb_str

    print('max_more_like', max_more_like)
    print('max_more_like type', type(max_more_like))
    print('max_more_like keys ', type(max_more_like.keys()))
    print('max_more_like keys type', max_more_like.keys())

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
                if max_more_like.__contains__(rgb):
                    stand_color = max_more_like.get(rgb).split(',')
                    im.putpixel([i, j], (int(stand_color[0]), int(stand_color[1]), int(stand_color[2])))

    # 最大的颜色集合
    max_color = []
    # 最大的颜色集合
    max_color_coordinate = {}
    # 最大最小颜色坐标
    max_color_min_max = {}

    for max_four_color in max_color_count_dict:
        max_color.append(max_four_color[0])
        max_color_coordinate[max_four_color[0]] = [];
        max_color_min_max[max_four_color[0]] = [];

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

    image_rgb_str_collection_new=[]
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
                image_rgb_str_collection_new.append(rgb)

    # 得到最大的四个像素的RGB逗号组装的 字符串 和 数量
    max_color_count_dict_new = collections.Counter(image_rgb_str_collection_new).most_common(max_color_number)

    print('max_four_new', max_color_count_dict_new)

    max_color_x_coordinate = []
    for k, v in max_color_coordinate.items():
#        max_color_min_max[k].append(min(v))
#        max_color_min_max[k].append(max(v))
#        max_color_x_coordinate.append(min(v))
#        max_color_x_coordinate.append(max(v))
        print(1)
    max_color_x_coordinate.sort()
    print('x_coordinate:', max_color_x_coordinate)
    return max_color_x_coordinate




if __name__ == "__main__":
    max_color_x_coordinate = get_color_coordinate_new('K2E2X9R5I0A6E4E8I7X8K1A5R0Q2X7E0.jpeg', 'down/')
