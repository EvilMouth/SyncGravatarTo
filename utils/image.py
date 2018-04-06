import requests
import os
from PIL import Image


def save_image(url, suffix='sgt'):
    file = 'temp_%s.png' % suffix
    r = requests.get(url, stream=True)
    with open(file, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    return os.path.abspath(file)


def save_image_jpg(url, suffix='sgt'):
    path = save_image(url, suffix)
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    path_jpg = path + '.jpg'
    rgb_im.save(path_jpg)
    delete_image(path)
    return path_jpg


def delete_image(path):
    os.remove(path)
