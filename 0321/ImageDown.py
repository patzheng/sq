# 批量下载验证码
import requests
import os
from os.path import isfile, join
from os import listdir
import random
import time
from PIL import Image
import shutil


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
    step = width / split_size;
    rgb_im = im.convert('RGB')
    for i in range(split_size):
        rgb_im.crop((i * step, 0, (i + 1) * step, height)).save(target_path + g_rand_file_name('jpeg'))  # 160，70


# 160，70
def split_image_new(filename, base_path='down/', split_size=4, target_path='split/'):
    im = Image.open(base_path + filename)
    rgb_im = im.convert('RGB')
    # for i in range(split_size):
    #m n e y
    rgb_im.crop((0, 0, 60, 70)).save(target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((61, 0, 92, 70)).save(target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((93, 0, 128, 70)).save(target_path + g_rand_file_name('jpeg'))  # 160，70
    rgb_im.crop((128, 0, 160, 70)).save(target_path + g_rand_file_name('jpeg'))  # 160，70


def coverL(filename, base_path='split/', target_path='gray/'):
    im = Image.open(base_path + filename).convert('L')
    im.save(target_path + g_rand_file_name('jpeg'))


def flow():
    down_base = 'down/'
    split_base = 'split/'
    gray_base = 'gray/'
    down_url = 'http://shixin.court.gov.cn/captcha.do'

    if os.path.exists(down_base):
        shutil.rmtree(down_base)
        shutil.rmtree(split_base)
        shutil.rmtree(gray_base)

    os.mkdir(down_base)
    os.mkdir(split_base)
    os.mkdir(gray_base)

    down_image(down_url, batch_size=4, sleep_time=2)

    down_images = [f for f in listdir(down_base) if isfile(join(down_base, f))]
    for file in down_images:
        print(file)
        split_image(filename=file)

    split_files = [f for f in listdir(split_base) if isfile(join(split_base, f))]
    for file in split_files:
        coverL(filename=file)


if __name__ == "__main__":
    split_image_new('X7U9O2U7L5X8U8G5H3N6S4S1V2V4I4A6.jpeg')
